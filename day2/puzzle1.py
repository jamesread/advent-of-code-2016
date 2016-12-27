#!/usr/bin/python

code = open('code', 'r').read()

pinpad = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

x = 1
y = 1

for line in code.strip().split("\n"):
    for instruction in line:
        if instruction == 'U' and y > 0: y -= 1
        if instruction == 'D' and y < 2: y += 1
        if instruction == 'L' and x > 0: x -= 1
        if instruction == 'R' and x < 2: x += 1

    print pinpad[y][x],
