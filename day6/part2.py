#!/usr/bin/python2

password = ""
contents = open('input', 'r').read().strip()

for index in range(0, 8):
    charFrequency = {}

    for line in contents.split("\n"):
        c = line[index]


        if c not in charFrequency:
            charFrequency[c] = 0

        charFrequency[c] = charFrequency[c] + 1


    smallest = 9999
    smallestChar = None

    for char, frequency in charFrequency.iteritems():
        if frequency < smallest:
            smallest = frequency
            smallestChar = char

    password += smallestChar

print password
