#!/usr/bin/python2

import sys

contents = open('input').read().strip()

def isValidAddress(address):
    rep = ""

    inBrackets = False

    foundCode = None

    for i in range(0, len(address) - 3):
        slidingWindow = address[i:i+4]

        if "[" in slidingWindow:
            inBrackets = True
            continue;
 
        if slidingWindow[0] == slidingWindow[3] and slidingWindow[1] == slidingWindow[2]:
            if slidingWindow[0] == slidingWindow[1] or slidingWindow[2] == slidingWindow[3]:
                continue

            if inBrackets:
                return False
            else: 
                foundCode = slidingWindow

        if inBrackets and slidingWindow[-1:] == "]":
            inBrackets = False
            continue
        
    if foundCode != None:
        print address, foundCode
        return True

    return False

#print isValidAddress("abba[mnop]qrst")
#print isValidAddress("abcd[bddb]xyyx")
#print isValidAddress("aaaa[qwer]tyui")
#print isValidAddress("ioxxoj[asdfgh]zxcvbn")
#sys.exit()

validAddresses = 0

for address in contents.split("\n"):
    if isValidAddress(address):
        validAddresses += 1;

print validAddresses
