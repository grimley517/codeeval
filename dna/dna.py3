import sys
from multiprocessing  import Pool

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

def shortern(sstring):
    ans = sstring[1::]
    return (ans)

def score2(startString, endString, scoreint, indel, stype):
    if stype==0:
        startString = shortern(startString)
        scoreint = scoreint - indelscore(indel)
        indel = True
    elif stype ==1:
        endString = shortern(endString)
        scoreint = scoreint - indelscore(indel)
        indel = True
    else:
        startString = shortern(startString)
        endString = shortern(endString)
        scoreint = scoreint - 3
        indel =  False
        
    ans = score(
                startString=startString,
                endString=endString,
                scoreint=scoreint,
                indel=indel)
    return (ans)

def score(startString, endString, scoreint=0, indel=False):

    if(len(startString) == 0 and len(endString) == 0):
        return (scoreint)
    elif (len(startString) == 0 or len(endString) == 0):
        remstring = startString + endString
        while len(remstring) > 0:
            scoreint -= indelscore(indel)
            indel=True
            remstring = shortern(remstring)
        return (scoreint)
    else:
        if matchLetter(startString[0], endString[0]):
            scoreint = score(
                    startString=shortern(startString),
                    endString=shortern(endString),
                    scoreint=scoreint + 3,
                    indel=False)
        else:
            P = Pool(3)
            ans = P.starmap(score2, [(startString, endString, scoreint, indel, 0),
                                           (startString, endString, scoreint, indel, 1),
                                           (startString, endString, scoreint, indel, 2)]
                                )
            scoreint = max(ans)
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
