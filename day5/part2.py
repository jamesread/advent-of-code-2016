#!/usr/bin/python2

import md5
import collections

Result = collections.namedtuple('Result', ['success', 'message'])

def md5hash(contents):
    md5er = md5.new()
    md5er.update(contents)

    return md5er.hexdigest()

def checkPasswordCharacterValid(generatedPassword, characterPosition, characterValue):
    if not str.isdigit(characterPosition):
        return Result(False, "position is not an int, ignoring")

    characterPosition = int(characterPosition)

    if characterPosition > len(generatedPassword) - 1:
        return Result(False, "position" + str(characterPosition) + " is too long! ignoring")

    if generatedPassword[characterPosition] != " ":
        return Result(False, "position" + str(characterPosition) + " already set, ignoring")

    return Result(True, None)

def crackPassword(doorId):
    index = 0
    generatedPassword = list("        ")

    while " " in generatedPassword:
        currentHash = md5hash(doorId + str(index))
        
        if currentHash.startswith("00000"):
            characterPosition = currentHash[5]
            characterValue = currentHash[6]

            print index, currentHash, characterPosition, characterValue

            checkCharacterResult = checkPasswordCharacterValid(generatedPassword, characterPosition, characterValue)

            if checkCharacterResult.success:
                generatedPassword[int(characterPosition)] = characterValue
            else:
                print checkCharacterResult.message

        index += 1

    return "".join(generatedPassword)
    
        
if __name__ == "__main__":
    doorId = open('input', 'r').read().strip()

    print crackPassword(doorId) 
