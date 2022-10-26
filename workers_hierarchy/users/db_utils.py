from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select, update, delete

from workers_hierarchy.users.tables import workers


__all__ = [
    'select_worker_by_id',
    'select_all_workers',
    'update_worker_by_id',
    'insert_worker',
    'delete_worker_by_id'
]


async def select_all_workers(conn):
    query = select(
        [
            workers.c.id,
            workers.c.first_name,
            workers.c.last_name,
            workers.c.surname,
            workers.c.position,
            workers.c.manager_id
        ]
    )
    cursor = await conn.execute(query)

    return await cursor.fetchall()


async def select_worker_by_id(conn, key):
    manager = workers.alias()
    query = select(
        [
            workers,
            manager.c.first_name.label('manager_first_name'),
            manager.c.last_name.label('manager_last_name'),
            manager.c.surname.label('manager_surname'),
            manager.c.id.label('id_manager')
        ])\
        .join(manager, workers.c.manager_id == manager.c.id)\
        .where(workers.c.id == key)
    cursor = await conn.execute(query)

    return await cursor.fetchone()


async def update_worker_by_id(conn, key, data):
    query = update(workers)\
        .where(workers.c.id == key)\
        .values(data)
    cursor = await conn.execute(query)

    return cursor


async def insert_worker(conn, data):
    query = insert(workers)\
            .values(data)\
            .on_conflict_do_nothing(constraint='const')\
            .returning(workers.c.id)
    cursor = await conn.execute(query)
    return await cursor.scalar()


async def delete_worker_by_id(conn, key):
    query = delete(workers)\
        .where(workers.c.id == key)
    cursor = await conn.execute(query)
    return cursor
