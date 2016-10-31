===================
agate-dbf |release|
===================

.. include:: ../README.rst

Install
=======

To install:

.. code-block:: bash

    pip install agate-dbf

For details on development or supported platforms see the `agate documentation <http://agate.readthedocs.org>`_.

Usage
=====

agate-dbf uses a monkey patching pattern to add read for dbf files support to all :class:`agate.Table <agate.table.Table>` instances.

.. code-block:: python

    import agate
    import agatedbf

    agatedbf.patch()

Calling :func:`.patch` attaches all the methods of :class:`.TableDBF` to :class:`agate.Table <agate.table.Table>`.

.. code-block:: python

    table = agate.Table.from_dbf('examples/test.dbf')

    print(table)

===
API
===

.. autofunction:: agatedbf.patch

.. autoclass:: agatedbf.table.TableDBF
    :members:

Authors
=======

.. include:: ../AUTHORS.rst

Changelog
=========

.. include:: ../CHANGELOG.rst

License
=======

.. include:: ../COPYING

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
