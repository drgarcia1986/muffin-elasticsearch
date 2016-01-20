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
