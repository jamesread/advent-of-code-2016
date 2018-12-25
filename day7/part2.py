#!/usr/bin/python2

import sys

contents = open('input').read().strip()

def isValidAddress(address):
    rep = ""

    inBrackets = False

    foundCode = None

    for i in range(0, len(address) - 3):
        slidingWindow = address[i:i+3]

        if "[" in slidingWindow:
            inBrackets = True
            continue;
 
        if slidingWindow[0] == slidingWindow[2] and slidingWindow[0] != slidingWindow[1]:
            if inBrackets:
                return False
            else: 
                oppositeCode = slidingWindow[1] + slidingWindow[0] + slidingWindow[1]

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
