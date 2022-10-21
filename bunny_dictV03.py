#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 16:47:58 2022

@author: srilthe
"""
import time

class Node(object):
    def __init__(self, location):
        self.location = location
        self.children = []

    def addChild(self, child):
        self.children.append(child)

def show_dict(dict_map, rows, cols):
    for r in rows:
        for c in cols:
            print(dict_map[(r, c)], end=' ')
        print()

def ard(a, b):
    return((a[0]+b[0], a[1]+b[1]))

def solution(map):
    dict_map = {}
    rows = range(len(map))
    cols = range(len(map[0]))
    for r in rows:
        for c in cols:
            dict_map[(r,c)] = map[r][c]
    remove_wall = [w for w,v in dict_map.items() if v == 1]
    cardinals = [[1, 0],[0,-1],[0, 1],[-1, 0]]
    trip_length = [999]
    MAX = r+c
    renovated = False
    show_dict(dict_map, rows, cols)
    for renovate in range(len(remove_wall)):
        if len(remove_wall) != 0:
            if renovated:
                dict_map.update({(remove_wall[renovate]): 0})
                dict_map.update({(remove_wall[renovate-1]): 1})
            else:
                dict_map.update({remove_wall[renovate]: 0})
                renovated = True
        start = (0, 0)
        root = Node(start)
        level = [root]
        traversed = [(0, 0)]
        arrived = False
        while arrived == False:
            for this_level in level:
                nextLevel = []
                for move in cardinals:
                    move_to = ard(this_level.location, move)
                    if (move_to) in dict_map.keys() \
                            and dict_map[(move_to)] == 0    \
                            and (move_to not in traversed):
                        traversed.append((move_to))
                        this_level.addChild(Node((move_to)))
            if len(this_level.children):
                for kid in this_level.children:
                    nextLevel.append(kid)
            else:
                arrived = True
            level = nextLevel
        if len(traversed) >= MAX:
            trip_length.append(len(traversed))
    return(min(trip_length))


start_time = time.time()
print(solution([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]]))
print(f"Time taken: {time.time() - start_time}")

start_time = time.time()
print(solution([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]]))
print(f"Time taken: {time.time() - start_time}")

start_time = time.time()
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]))
print(f"Time taken: {time.time() - start_time}")
