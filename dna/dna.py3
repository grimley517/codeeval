import sys


def matchLetter(letterA, letterB):
    return (letterA == letterB)

def indelscore(indelstate):
    if indelstate:
        return 1
    else:
        return 8

def clean(instring):
    allowed = "ACGT"
    answer = ""
    instring = instring.upper()
    for letter in instring:
        if letter in allowed:
            answer += letter
    return (answer)

def score(startString, endString, indel=False):
    oneago = []
    thisrow = list(range(1, len(endString) + 1)) + [0]
    for x in list(range(len(startString))):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(endString) + [x + 1]
        for y in list(range(len(endString))):
            delcost = oneago[y] - 3
            addcost = thisrow[y - 1] - 3
            subcost = oneago[y - 1] + (startString[x] != endString[y])
            thisrow[y] = min(delcost, addcost, subcost)
            print(thisrow)
    return thisrow[len(seq2) - 1]


if __name__ == "__main__":
    with open(sys.argv[1], "rt") as myfile:
        lines = myfile.read()
        try:
            for line in lines:
                parts = line.split("|")
                partA = clean(parts[0])
                partB = clean(parts[1])
            print(score(startString=partA, endString=partB))
        except:
            print(lines)
