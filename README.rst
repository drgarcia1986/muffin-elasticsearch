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

.. _installation:

Installation
=============

**Muffin-ElasticSearch** should be installed using pip: ::

    pip install git+https://github.com/drgarcia1986/muffin-elasticsearch.git

.. _usage:

Usage
=====

Add *muffin-ElasticSearch* to muffin plugin list:

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
        def get(self, request):
            ret = yield from app.ps.elasticsearch.get(
                index='my-index',
                doc_type='test-type',
                id=42
            )
            return ret

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
