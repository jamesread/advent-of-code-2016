#!/usr/bin/python

import sys

instructions = open("input", "r").read()

bearing = 0 # 0 = north, 90 = east, south = 180, west = 270
x = 0
y = 0;

visited = []

for instruction in instructions.split(", "):
    direction = instruction[0:1]
    distance = int(instruction[1:])

    if direction == 'L': bearing -= 90
    elif direction == 'R': bearing += 90
    else: raise ValueError(direction);

    if bearing == 360: bearing = 0
    if bearing == -90: bearing = 270

    for step in range(0, distance):
        if bearing == 0: x += 1
        if bearing == 90: y += 1
        if bearing == 180: x -= 1
        if bearing == 270: y -= 1

        currentCoords = "%d %d" % (x, y)

        if currentCoords in visited:
            print "Headquarters appears to be at: " + currentCoords + " because we visited it already."
            sys.exit(0)
        else:
            visited.append(currentCoords)

    print "dir:%s dist:%s -> bearing:%s x,y:%s:%s " % (direction, distance, bearing, x, y)

