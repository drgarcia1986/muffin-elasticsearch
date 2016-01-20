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


def test_should_raise_type_error_for_invalid_configuration(loop):
    with pytest.raises(TypeError):
        muffin.Application(
            'test', loop=loop, PLUGINS=['muffin_elasticsearch']
        )


@pytest.mark.async
def test_elasticsearch_create_get(app):
    body = {'str': 'foo', 'int': 1}
    result = yield from app.ps.elasticsearch.create(
        index='test',
        doc_type='test',
        id=42,
        body=body
    )

    assert result['ok'] is True

    result = yield from app.ps.elastisearch.get(
        index='test',
        doc_type='test',
        id=42
    )
    assert result['_source'] == body
