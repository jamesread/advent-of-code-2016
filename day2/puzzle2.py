#!/usr/bin/python

code = open('code', 'r').read()

pinpad = [
    [ 0, 0, 1, 0, 0 ],
    [ 0, 2, 3, 4, 0 ],
    [ 5, 6, 7, 8, 9 ],
    [ 0, 'A', 'B', 'C', 0 ],
    [ 0, 0, 'D', 0, 0 ],
]

x = 0
y = 2

for line in code.strip().split("\n"):
    for instruction in line:
        deltaX = 0
        deltaY = 0

        if instruction == 'U': deltaY = -1
        if instruction == 'D': deltaY = +1
        if instruction == 'L': deltaX = -1
        if instruction == 'R': deltaX = +1

        newX = x + deltaX
        newY = y + deltaY

        if newX < 0 or newX > 4 or newY < 0 or newY > 4: 
            continue
        elif pinpad[newY][newX] == 0:
            continue
        else:
            x = newX
            y = newY

    print pinpad[y][x],
