#!/usr/bin/python

instructions = open("input", "r").read()

bearing = 0 # 0 = north, 90 = east, south = 180, west = 270
x = 0
y = 0;

for step in instructions.split(", "):
    direction = step[0:1]
    distance = int(step[1:])

    if direction == 'L':
        bearing -= 90
    elif direction == 'R':
        bearing += 90
    else:
        raise ValueError(direction);

    if bearing == 360:
        bearing = 0

    if bearing == -90:
        bearing = 270



    if bearing == 0:
        x += distance

    if bearing == 90:
        y += distance

    if bearing == 180:
        x -= distance

    if bearing == 270:
        y -= distance

    print "dir:%s dist:%s -> bearing:%s x,y:%s:%s " % (direction, distance, bearing, x, y)
