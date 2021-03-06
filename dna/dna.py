import sys
from functools import lru_cache

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

@lru_cache(maxsize= None)
def score(startString, endString, scoreint=0, indel=False):

    if(len(startString) == 0 and len(endString) == 0):
        return (scoreint)
    elif (len(startString) == 0 or len(endString) == 0):
        remstring = startString + endString
        while len(remstring) > 0:
            scoreint -= indelscore(indel)
            indel=True
            remstring = remstring[1::]
        return (scoreint)
    else:
        if matchLetter(startString[0], endString[0]):
            scoreint = score(
                    startString=startString[1::],
                    endString=endString[1::],
                    scoreint=scoreint + 3,
                    indel=False)
        else:
            maxi = scoreint-10
            ans3 = score(
                    startString=startString[1::],
                    endString=endString,
                    scoreint=scoreint - indelscore(indel),
                    indel=True)
            if ans3:
                maxi=ans3
            ans4 = score(
                    startString=startString,
                    endString=endString[1::],
                    scoreint=scoreint - indelscore(indel),
                    indel=True)
            if ans4 and ans4>maxi:
                maxi = ans4
            ans5 = score(
                    startString=startString[1::],
                    endString=endString[1::],
                    scoreint=scoreint - 3,
                    indel=False)
            if ans5 and ans5>maxi:
                maxi = ans5
            scoreint = maxi
        return (scoreint)


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
