#!/usr/bin/env python

import agate

import agatedbf

table = agate.Table.from_dbf('examples/test.dbf')

print(table)
table.print_table()
