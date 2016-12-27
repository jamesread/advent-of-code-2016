#!/usr/bin/python 

content = open('input', 'r').read().strip()

validTriangles = 0

for candidateTriangle in content.split("\n"):
    sideLengths = []

    for fragment in candidateTriangle.split(" "):
        if fragment == "": continue;

        sideLengths.append(int(fragment.strip()))

    sideLengths.sort()
    
    if sideLengths[0] + sideLengths[1] > sideLengths[2]:
        validTriangles += 1

print str(validTriangles) + " valid triangles found."
