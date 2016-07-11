import asyncio

from aioes import Elasticsearch
from muffin.plugins import BasePlugin


__version__ = "0.0.2"
__project__ = "muffin-elasticsearch"
__author__ = "Diego Garcia <drgarcia1986@gmail.com>"
__license__ = "MIT"


class Plugin(BasePlugin):

    """ Connect to ElasticSearch. """

    name = 'elasticsearch'
    defaults = {
        'endpoints': ['localhost:9200'],
    }

    def __init__(self, *args, **kwargs):
        """ Initialize the Plugin. """
        super().__init__(*args, **kwargs)
        self.conn = None

    def setup(self, app):
        """ Setup self. """
        super().setup(app)

    @asyncio.coroutine
    def start(self, app):
        """ Connect to ElasticSearch. """
        self.conn = Elasticsearch(self.cfg.endpoints)

    def finish(self, app):
        """ Close self connections. """
        self.conn.close()

    def __getattr__(self, name):
        """ Proxy attribute to self connection. """
        return getattr(self.conn, name)
