from datetime import date
import aiohttp_jinja2
from aiohttp import web

from workers_hierarchy.users.db_utils import (
    select_worker_by_id,
    insert_worker,
    select_all_workers,
    update_worker_by_id,
    delete_worker_by_id
)
from workers_hierarchy.utils.views_utils import (
    get_hierarchy,
    validate_data,
    validate_delete
)


@aiohttp_jinja2.template('all_workers.html')
async def get_all_workers(request):
    engine = request.app['db']
    async with engine.acquire() as conn:
        workers = await select_all_workers(conn)
    if workers:
        parents = sorted(workers, key=lambda x: (x['manager_id'], x['id']))
        hierarchy = list(get_hierarchy(parents, parents).items())[0]
        hierarchy = {hierarchy[0]: hierarchy[1]}
        parents = {parent.id: parent for parent in parents}
    else:
        parents = []
        hierarchy = []
    return {"parents": parents, "hierarchy": hierarchy}


@aiohttp_jinja2.template('worker.html')
async def get_worker(request):
    engine = request.app['db']
    async with engine.acquire() as conn:
        worker_id = request.match_info['id']
        worker = await select_worker_by_id(conn, worker_id)
    return {"worker": worker}


@aiohttp_jinja2.template('update_worker.html')
async def update_worker(request):
    engine = request.app['db']
    worker_id = request.match_info['id']
    today_date = str(date.today().strftime("%Y-%m-%d"))

    if request.method == 'GET':
        async with engine.acquire() as conn:
            worker = await select_worker_by_id(conn, worker_id)
            worker = dict(worker)
            workers = await select_all_workers(conn)
            return {"worker": worker, "workers": workers, "date": today_date}

    elif request.method == 'POST':
        data = await request.post()
        error = validate_data(data)
        if error:
            async with engine.acquire() as conn:
                workers = await select_all_workers(conn)
            data = dict(data)
            data['id'] = worker_id
            return {
                "worker": data,
                "workers": workers,
                "date": today_date,
                "error": error
            }
        else:
            async with engine.acquire() as conn:
                worker_id = request.match_info['id']
                await update_worker_by_id(conn, worker_id, data)
                location = request.app.router['worker'].url_for(id=worker_id)
                raise web.HTTPFound(location=location)


@aiohttp_jinja2.template('create_worker.html')
async def create_worker(request):
    engine = request.app['db']
    today_date = date.today().strftime("%Y-%m-%d")

    if request.method == 'GET':
        async with engine.acquire() as conn:
            workers = await select_all_workers(conn)
            return {"workers": workers, 'date': today_date, "error": None}

    elif request.method == 'POST':
        data = await request.post()
        error = validate_data(data)
        if error:
            async with engine.acquire() as conn:
                workers = await select_all_workers(conn)
            return {"workers": workers, "date": today_date, "error": error}
        else:
            async with engine.acquire() as conn:
                new_worker_id = str(await insert_worker(conn, data))
                location = request.app.router['worker'].url_for(id=new_worker_id)
                raise web.HTTPFound(location=location)


@aiohttp_jinja2.template('delete_worker.html')
async def delete_worker(request):
    engine = request.app['db']
    worker_id = request.match_info['id']

    if request.method == 'GET':
        async with engine.acquire() as conn:
            worker = await select_worker_by_id(conn, worker_id)
            return {"worker": worker, "error": None}

    elif request.method == 'POST':
        check = await validate_delete(engine)
        if check:
            async with engine.acquire() as conn:
                try:
                    await delete_worker_by_id(conn, worker_id)
                except Exception:
                    error = "Please change manager for all direct subordinates"
                    return {"error": error, "worker": None}
                location = request.app.router['workers'].url_for()
                raise web.HTTPFound(location=location)
        else:
            error = "You can't delete all workers because there will be no company."
            return {"error": error, "worker": None}
