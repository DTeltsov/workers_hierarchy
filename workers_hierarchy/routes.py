import pathlib
from workers_hierarchy.main.views import (
    get_all_workers,
    get_worker,
    update_worker,
    create_worker,
    delete_worker
)

PROJECT_PATH = pathlib.Path(__file__).parent


def init_routes(app):
    add_route = app.router.add_route

    add_route('*', '/', get_all_workers, name='workers')
    add_route('*', '/worker/create', create_worker, name='create-worker')
    add_route('*', '/worker/{id}', get_worker, name='worker')
    add_route('*', '/worker/{id}/update', update_worker, name='update-worker')
    add_route('*', '/worker/{id}/delete', delete_worker, name='delete-worker')


    # added static dir
    app.router.add_static(
        '/static/',
        path=(PROJECT_PATH / 'static'),
        name='static',
    )
