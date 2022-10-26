
from aiohttp import web

from .app import init_app
import aiohttp_debugtoolbar


def create_app():
    app = init_app()
    aiohttp_debugtoolbar.setup(
        app,
        check_host=False,
        intercept_redirects=False)

    return app


def main() -> None:
    app = init_app()
    app_settings = app['config']['app']
    web.run_app(
        app,
        host=app_settings['host'],
        port=app_settings['port'],
    )


if __name__ == '__main__':
    main()
