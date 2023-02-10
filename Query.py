#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 2023

@author: srilthe

Import a CSV file with Pandas and use it's information
to transfer data into SQL
# Generating the creation of table

CREATE TABLE assetz ( 
    Name VARCHAR(53), 
    Quantity INT(7), 
    Value FLOAT(6), 
    Container VARCHAR(45)
    )

# and the insert commands, filling the table
INSERT INTO assets (Name, Quantity, Value, Container)
 VALUES ("Zorn Star Ingot", 265, 7.95, "STORAGE (Planet Cyrene)")

"""

from getpass import getpass
from mysql.connector import connect, Error
import pandas as pd

def query_execute(cmd):
    print(f"{cmd}")
    try:
        query.execute(cmd)
        for i in query:
            print(i)
    except Error as e:
        print(f"{e}\n\n")

def dblq(ar):
    b = '\"'
    e = '\",'
    dbl = ""
    for i in ar[:-1]:
        if isinstance(i, str):
            dbl += f"{b}{i}{e}"
        else:
            dbl += f"{i},"
    if isinstance(ar[-1], str):
        dbl += f"{b}{ar[-1]}{b}"
    else:
        dbl += f"{ar[-1]}"
    return (dbl)

def noqs(ar):
    noq = ""
    for i in ar[:-1]:
        noq += f"{i}, "
    noq += f"{ar[-1]}"
    return (noq)


mydb = connect(
    host="localhost",
    user=input("Enter username: "),
    password=getpass("Enter Password: "),
    database="entropia"
)
query = mydb.cursor()

# Dictionary map data type pandas to sql
map_types = {'object': 'VARCHAR', 'int64': 'INT', 'float64': 'FLOAT'}

df = pd.read_csv('./Data/EU-Assets.csv')
info_ar = []
dfd = df.dtypes
for c, i in enumerate(list(df.columns.values)):
    info_ar.append([i, max(df[i].astype(str).map(len)), str(dfd[c])])

names = tuple(df.columns.values)
Values = [f"{i} {map_types[info_ar[c][2]]}({info_ar[c][1]})" for c, i in enumerate(names)]
make_table = ["CREATE TABLE assetz ("]
for i in Values[:-1]:
    make_table.append(f"{i},")
make_table.append(f"{Values[-1]})")

create_table = str(tuple(make_table)).replace("'", "").replace(",,", ",").replace("(,", "(").replace(")))", "))")
query_execute(f"{create_table[1:]}")

for index, row in df.iterrows():
    if index < len(df):
        query_execute(f"INSERT INTO assetz ({noqs(names)}) VALUES ({dblq(tuple(row))})")
mydb.commit()
