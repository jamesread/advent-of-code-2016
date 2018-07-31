#!/usr/bin/python2

import md5

def md5hash(contents):
    md5er = md5.new()
    md5er.update(contents)

    return md5er.hexdigest()

doorId = open('input', 'r').read().strip()

index = 0
generatedPassword = ""

while len(generatedPassword) != 8:
    toHash = doorId + str(index)
    currentHash = md5hash(toHash)
    
    if currentHash.startswith("00000"):
        print index, currentHash, currentHash[5]

        generatedPassword += currentHash[5]

    index += 1
        
print generatedPassword
