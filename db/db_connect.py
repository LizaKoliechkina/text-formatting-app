import typing as t

import asyncpg
from aiohttp import web
from loguru import logger

import config


async def install(app: web.Application) -> t.AsyncIterator[None]:
    logger.debug('Installing database engine')

    app['db'] = await asyncpg.connect(
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        database=config.POSTGRES_DB,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
    )
    logger.debug('Database engine ready')

    yield

    logger.debug('Closing database engine')
    await app['db'].close()
