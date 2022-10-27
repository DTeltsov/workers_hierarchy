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
