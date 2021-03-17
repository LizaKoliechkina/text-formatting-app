import typing as t

from aiohttp import web, ClientSession
from loguru import logger


async def install(app: web.Application) -> t.AsyncIterator[None]:
    logger.debug('Initializing client session.')
    app['session'] = ClientSession()
    yield

    logger.debug('Closing session')
    await app['session'].close()
