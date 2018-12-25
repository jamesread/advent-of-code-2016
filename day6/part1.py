#!/usr/bin/python2

contents = open('input', 'r').read().strip()

for index in range(0, 8):
    charFrequency = {}

    for line in contents.split("\n"):
        c = line[index]


        if c not in charFrequency:
            charFrequency[c] = 0

        charFrequency[c] = charFrequency[c] + 1


    biggest = 0
    biggestChar = None

    for char, frequency in charFrequency.iteritems():
        if frequency > biggest:
            biggest = frequency
            biggestChar = char

    print biggestChar,
