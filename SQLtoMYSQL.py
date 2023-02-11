#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:14:45 2023

@author: srilthe

https://sample-videos.com/download-sample-sql.php

won't create table yet but will display create table text
insert into needs to be completed 

can use Query.py to finish automating
"""

import locale
import textwrap
import io

file = "Data/Sample-SQL-File-1000rows.sql"


def guess_encoding(file):
    """guess the encoding of the given file"""
    with io.open(file, "rb") as f:
        data = f.read(5)
    if data.startswith(b"\xEF\xBB\xBF"):  # UTF-8 with a "BOM"
        return "utf-8-sig"
    elif data.startswith(b"\xFF\xFE") or data.startswith(b"\xFE\xFF"):
        return "utf-16"
    else:
        try:
            with io.open(file, encoding="utf-8") as f:
                return ("utf-8")
        except Exception as e:
            print(e)
            return locale.getdefaultlocale()[1]

def create_query_string(f):
    with open(f, 'r', encoding=guess_encoding(f)) as f_in:
        lines = f_in.read()
        query_string = textwrap.dedent("""{}""".format(lines))
        return (query_string)
        print('Found the file and created a converted string.')


qs = create_query_string(file)
create_table_start = qs.find("CREATE TABLE")
create_table_end = qs[create_table_start:].find(";")
insert_cmd_start = qs.find("INSERT INTO")
insert_fields_start = qs[insert_cmd_start:].find("(") + insert_cmd_start
insert_cmd_end = qs[insert_cmd_start:].find(")") + insert_cmd_start + 1


print(qs[create_table_start:create_table_end + create_table_start])
print()
print(qs[insert_cmd_start:insert_cmd_end])
print()
data_fields = qs[insert_fields_start:insert_cmd_end][1:-1].replace("`","").split(", ")
print(len(data_fields), data_fields)
print()
values_start = qs.find("VALUES") + 6
print(f"VALUES: starts at {values_start}")

data_rows = qs[values_start+1:].split(",\n")

# mysql requires "double-quotes" around text values
converted_rows = []
for row in data_rows:
    converted_rows.append(str(tuple(row[1:-3].split(", "))).replace("'", ""))
print()
print(converted_rows[-1])

"""


"""
