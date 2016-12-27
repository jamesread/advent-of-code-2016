#!/usr/bin/python 

content = open('input', 'r').read().strip().split("\n")
contentList = []

validTriangles = 0

for candidateTriangle in content:
    sideLengths = []

    for fragment in candidateTriangle.split(" "):
        if fragment == "": continue;

        sideLengths.append(int(fragment.strip()))

    contentList.append(sideLengths)
   
for row in range(0, len(contentList) / 3):
    for col in range(0, 3):
        values = []
        values.append(contentList[(row * 3)+0][col])
        values.append(contentList[(row * 3)+1][col])
        values.append(contentList[(row * 3)+2][col])
        values.sort()

        print values

        if values[0] + values[1] > values[2]:
            validTriangles += 1

print str(validTriangles) + " valid triangles found, out of " + str(len(contentList))
