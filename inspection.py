#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:03:53 2022

@author: srilthe
"""
#  * *
import os
import sys
import inspect
import numpy as np

def main(dr):
    for test in dir(inspect):
        if test[0] != "_" and test != "__nonzero__":
            if "is" == test[:len(test)-(len(test)-2)]:
                for c, i in enumerate(dr):
                    if eval(f"inspect.{test}({i})"):
                        print(f"{c}:{i} is a {test[2:]}")


def myFun():
    print("I'm a function")


if __name__ == '__main__':
    main(dir())

#  OUTPUT:
"""

5:__nonzero__ is a function
9:main is a function
10:myFun is a function
8:inspect is a module
11:np is a module
12:os is a module
13:sys is a module
5:__nonzero__ is a routine
9:main is a routine
10:myFun is a routine

"""
