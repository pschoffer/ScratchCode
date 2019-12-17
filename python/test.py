# A precedence rule is given as "P>E",
# which means that letter "P" is followed directly by the letter "E".
# Write a function, given an array of precedence rules, that finds the word represented by the given rules.

# Note: Each represented word contains a set of unique characters, i.e. the word does not contain duplicate letters.

# Examples:
# findWord(["P>E","E>R","R>U"]) // PERU
# findWord(["I>N","A>I","P>A","S>P"]) // SPAIN


def convertToDict(rules):
    result = dict()
    for rule in rules:
        key = rule[0]
        result[key] = rule[1]
    return result


def composeWord(start, area):
    current = start
    last = None
    word = ""
    while current in area:
        word += current
        current = area[current]
    word += current
    return word


def findWord(rules):
    parsedRules = list(map(lambda ruleStr: (ruleStr[0], ruleStr[2]), rules))
    letterArea = convertToDict(parsedRules)
    slaves = set()
    for key in letterArea:
        slaves.add(letterArea[key])
    master = None
    for key in letterArea:
        if key not in slaves:
            master = key
    return composeWord(master, letterArea)


print(findWord(["P>E", "E>R", "R>U"]))
print(findWord(["I>N", "A>I", "P>A", "S>P"]))
print(findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]))  # HUNGARY
print(findWord(["I>F", "W>I", "S>W", "F>T"]))  # // SWIFT
# // PORTUGAL
print(findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))
print(findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R",
                "L>A", "A>N", "N>D", "I>T"]))  # // SWITZERLAND
