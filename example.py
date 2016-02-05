#!/usr/bin/env python

import agate
import agatedbf

agatedbf.patch()

table = agate.Table.from_dbf('examples/test.dbf')

print(table)
table.print_table()
