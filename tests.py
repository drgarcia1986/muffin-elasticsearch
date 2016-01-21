import muffin
import pytest


@pytest.fixture(scope='session')
def app(loop):
    return muffin.Application(
        'elasticsearch_app', loop=loop,
        PLUGINS=('muffin_elasticsearch',)
    )


def test_plugin_register(app):
    assert 'elasticsearch' in app.ps
    assert app.ps.elasticsearch.conn


@pytest.mark.async
def test_elasticsearch_create_get(app):
    body = {'str': 'foo', 'int': 1}
    result = yield from app.ps.elasticsearch.create(
        index='test',
        doc_type='test',
        id=42,
        body=body
    )

    assert 'created' in result, result.keys()
    assert result['created'] is True, result['created']

    result = yield from app.ps.elasticsearch.get(
        index='test',
        doc_type='test',
        id=42
    )
    assert '_source' in result, result.keys()
    assert result['_source'] == body, result
