from aiohttp import web
from loguru import logger

import server
import session
from db import db_connect


def init() -> web.Application:

    app = web.Application()

    server.install(app)

    app.cleanup_ctx.append(db_connect.install)
    app.cleanup_ctx.append(session.install)

    return app


if __name__ == '__main__':
    try:
        logger.info('Initializing the application')
        app = init()
        web.run_app(app)
    except Exception:
        logger.exception('Failed to initialize')
