#!/usr/bin/env python
# -*- coding: utf8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import agate
import agatedbf

class TestDBF(agate.AgateTestCase):
    def setUp(self):
        self.table = agate.Table.from_csv('examples/testdbf_converted.csv')

    def test_from_dbf(self):
        table = agate.Table.from_dbf('examples/test.dbf')

        self.assertColumnNames(table, self.table.column_names)
        self.assertColumnTypes(table, [t.__class__ for t in self.table.column_types])
        self.assertRows(table, self.table.rows)
