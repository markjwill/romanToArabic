def romanToInt(romanString):
    romansDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "G": 5000,
        "H": 10000
    }

    values = []
    for char in romanString:
        values.append(romansDict[char])

    finalValue = 0
    intermediateValue = 0

    firstPosition = 0

    for thisPosition in range(len(values)):
        previousIsEqual = False
        previousIsGreater = False
        previousIsLess = False
        if thisPosition > firstPosition:
            if values[thisPosition-1] == values[thisPosition]:
                previousIsEqual = True
            elif values[thisPosition-1] > values[thisPosition]:
                previousIsGreater = True
            else:
                previousIsLess = True
        else:
            intermediateValue = values[thisPosition]

        if previousIsEqual:
            intermediateValue += values[thisPosition]

        if previousIsGreater:
            finalValue += intermediateValue
            intermediateValue = 0
            intermediateValue += values[thisPosition]

        if previousIsLess:
            finalValue -= intermediateValue
            intermediateValue = 0
            intermediateValue += values[thisPosition]

    finalValue += intermediateValue

    return finalValue

tests = [
    "II",
    "IV",
    "VIII",
    "LXXXIX",
    "XCII"
]

for string in tests:
    print("\n")
    print("Input: "+string)
    print("Output: " + str(romanToInt(string)))
