===================
agate-dbf |release|
===================

.. include:: ../README.rst

Install
=======

To install:

.. code-block:: bash

    pip install agate-dbf

For details on development or supported platforms see the `agate documentation <https://agate.readthedocs.org>`_.

Usage
=====

agate-dbf uses a monkey patching pattern to add read for dbf files support to all :class:`agate.Table <agate.table.Table>` instances.

.. code-block:: python

    import agate
    import agatedbf

Importing agate-dbf adds new methods to :class:`agate.Table <agate.table.Table>`.

.. code-block:: python

    table = agate.Table.from_dbf('examples/test.dbf')

    print(table)

===
API
===

.. autofunction:: agatedbf.table.from_dbf

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
