Muffin-ElasticSearch
############

.. _description:

Muffin-ElasticSearch -- A simple ElasticSearch plugin for muffin_ framework.

.. _badges:

.. image:: http://img.shields.io/travis/drgarcia1986/muffin-elasticsearch.svg?style=flat-square
    :target: http://travis-ci.org/drgarcia1986/muffin-elasticsearch
    :alt: Build Status

.. _requirements:

Requirements
=============

- python >= 3.4
- muffin >= 0.5.5
- aioes == 0.4

.. _installation:

Installation
=============

**Muffin-ElasticSearch** should be installed using pip: ::

    pip install muffin-elasticsearch

.. _usage:

Usage
=====

Add *muffin-elasticsearch* to muffin plugin list:

.. code-block:: python

    import muffin


    app = muffin.Application(
        'example',

        PLUGINS=(
            'muffin_elasticsearch',
        )
    )

And use *ElasticSearch* plugin:

.. code-block:: python

    @app.register('/search')
    class Example(muffin.Handler):

        @asyncio.coroutine
        def post(self, request):
            body = yield from request.json()
            result = yield from app.ps.elasticsearch.create(
                index='my-index',
                doc_type='test',
                id=42,
                body=body
            )
            return muffin.json_response(
                data=result, status=201
            )


        @asyncio.coroutine
        def get(self, request):
            ret = yield from app.ps.elasticsearch.get(
                index='my-index',
                doc_type='test-type',
                id=42
            )
            return muffin.json_response(data=result)


.. _options:

Options
-------

========================== ==============================================================
 *ELASTICSEARCH_ENDPOINTS* List of ElasticSearch servers (``['localhost:9200']``)
========================== ==============================================================

.. _bugtracker:

Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/drgarcia1986/muffin-elasticsearch/issues

.. _contributing:

Contributing
============

Development of Muffin-ElasticSearch happens at: https://github.com/drgarcia1986/muffin-elasticsearch


Contributors
=============

* drgarcia1986_ (Diego Garcia)

.. _license:

License
=======

Licensed under a `MIT license`_.

.. _links:


.. _muffin: https://github.com/klen/muffin
.. _drgarcia1986: https://github.com/drgarcia1986
.. _MIT license: http://opensource.org/licenses/MIT
