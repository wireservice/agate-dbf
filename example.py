#!/usr/bin/env python

import agate
import agatedbf

agatedbf.patch()

table = agate.Table.from_dbf('examples/test.dbf')

table.print_structure()
table.print_table()
