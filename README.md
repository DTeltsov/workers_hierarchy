# workers_hierarchy
Little webpage, which displays all workers and their hierarchy.
Created useing Python, aiohttp, PostgreSQL, Alembic and [create-aio-app](https://github.com/aio-libs/create-aio-app) boilerplate generator.

## Usage

### First Build
```bash
make run
```
And when server is up, run this two commands
```bash
make migrations
make migrate

```

### To stop
```bash
make stop
```

### To run
```bash
make run
```

### To stop and delete container
```bash
make clean
```

## Structure

- In [routes.py](https://github.com/DTeltsov/workers_hierarchy/blob/master/workers_hierarchy/routes.py) you can find all routes and coresponding views.
- In [views.py](https://github.com/DTeltsov/workers_hierarchy/blob/master/workers_hierarchy/main/views.py) you can find all views and in [views_utils.py](https://github.com/DTeltsov/workers_hierarchy/blob/master/workers_hierarchy/utils/views_utils.py) you can find all related utils.
- In [db_utils.py](https://github.com/DTeltsov/workers_hierarchy/blob/master/workers_hierarchy/users/db_utils.py) you can find all db-related functions, which are used in views.
- In [tables.py](https://github.com/DTeltsov/workers_hierarchy/blob/master/workers_hierarchy/users/tables.py) you can find tables declarations.
