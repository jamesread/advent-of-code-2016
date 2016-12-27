#!/usr/bin/python

import re
import operator

def letterRank(roomName):
    letters = {}

    uniques = list(set(roomName))
    counts = [roomName.count(letter) for letter in uniques]

    letterRanks = dict(zip(uniques, counts))
    letterRanks = sorted(letterRanks.items(), key = lambda(k, v): (-v, k), reverse = False)

    return letterRanks

def checkChecksum(letterRanks, checksum):
    for i in range(0, len(checksum)):
        if letterRanks[i][0] != checksum[i]:
            return False

    return True

def addAndWrap(original, add, limit):
    while add > 0:
        add -= 1
        original += 1

        if original == limit:
            original = 0
    
    return original 

def translateRoomName(roomName, code):
    real = ""

    for char in roomName:
        if char == "-": real += " "; continue

        newChar = addAndWrap(ord(char) - 97, code, 26)
        real += chr(97 + newChar)

    return real

def assertValid(roomName, checksum):
    ranks = letterRank(roomName.replace("-", ""))

    res = checkChecksum(ranks, checksum)

    if not res:
        print ranks
        raise Exception("room not valid " + roomName)

assertValid("aaaaa-bbb-z-y-x", "abxyz")

content = open('input', 'r').read().strip().split("\n");
total = 0

for line in content:
    m = re.search("(?P<roomName>.+)-(?P<roomCode>\d+)\[(?P<checksum>.+)\]", line)

    if not m:
        print "No match on line;", line

    ranks = letterRank(m.group('roomName').replace("-", ""))

    if checkChecksum(ranks, m.group('checksum')):
        code = int(m.group('roomCode'))

        print "   " + translateRoomName(m.group('roomName'), code)

        total += code

        print "Valid:", line
    else:
        print "Invalid:", line


print total
