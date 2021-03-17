import typing as t

from aiohttp import web
from aiohttp_validate import validate

from server.format import apply_filter
from db import query as q
from db.db_session import get_db_session
from db import schemas as sch


def install(app: web.Application):
    app.router.add_post('/format', format_text)
    app.router.add_get('/status', request_status)


@validate(
    request_schema={
        'type': 'object',
        'description': 'Schema for formatText request',
        'properties': {
            'text': {
                'type': 'string',
                'minLength': 2,
                'maxLength': 2000
            },
            'filters': {
                'type': 'array',
                'items': {
                    'type': 'string',
                    'enum': ['capitalize', 'upper', 'lower', 'title', 'strange_format']
                }
            },
            'progress_url': {
                'type': 'string',
            }
        },
        'required': ['text', 'filters']
    },
)
async def format_text(body: t.Dict, request: web.Request) -> web.Response:
    # aiohttp_validate returns request body after validation
    text = body['text']
    filters = body['filters']
    url = body.get('progress_url', '')

    with get_db_session() as db_ses:
        obj = q.save_element(text, db_ses)
        obj_id = obj.id

        for f in filters:
            formatted = apply_filter(text, f)
            format_hist = sch.History(
                text_id=obj_id,
                formatted=formatted,
                filter=f,
                queue=filters.index(f),
            )
            q.save_format_history(format_hist, db_ses)

            if url:
                await request.app['session'].post(url, data=formatted)

        q.update_request_status(obj_id, db_ses)
    return web.json_response(data={
        'info': f'Received text format request {obj_id}',
        'text': text,
    })


async def request_status(request: web.Request) -> web.Response:
    try:
        request_id = int(request.query['id'])
    except KeyError:
        return web.json_response(data='Please provide request id')

    if request_id:
        with get_db_session() as db_ses:
            element = q.get_element(request_id, db_ses)
            if element is None:
                return web.json_response(data=f'Element with id {request_id} not found')
            history = q.get_history(request_id, db_ses)
        return web.json_response(data={
            'original': element.text,
            'status': 'Done' if element.done else 'In Progress',
            'formatting history': [{
                'id': h.queue,
                'filter': h.filter,
                'text': h.formatted,
            } for h in history],
        })
