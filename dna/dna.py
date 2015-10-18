import sys

def matchLetter(letterA, letterB):
    if (letterA == letterB):
        return (True)
    else:
        return (False)
        

def score(startString, endString, scoreint =0, indel= False):
    
    if(len(startString)==0 and len(endString) == 0):
        return (scoreint)
    elif (len(startString)==0 or len(endString) == 0):
        remstring = startString + endString
        while len(remstring)>0:
            if indel:
                scoreint -= 1
                indel=True
            else:
                scoreint -= 8
                indel = True
            remstring = remstring[1::]
        return scoreint
    else:
        if matchLetter(startString[0], endString[0]):
            scoreint = score(
                            startString=startString[1::],
                            endString=endString[1::],
                            scoreint=scoreint +3,
                            indel=False)
        elif(indel):
            consider = []
            ans1 = score(
                        startString=startString[1::],
                        endString=endString,
                        scoreint=scoreint -1,
                        indel=True)
            if ans1:
                consider.append(ans1)
            ans2 = score(
                        startString=startString,
                        endString=endString[1::],
                        scoreint=scoreint -1,
                        indel=True)
            if ans2:
                consider.append(ans2)
            ans5 = score(
                        startString=startString[1::],
                        endString=endString[1::],
                        scoreint=scoreint -3,
                        indel=False)
            if ans5:
                consider.append(ans5)
            scoreint = max(consider)
        else:
            consider = []
            ans3 = score(
                        startString=startString[1::],
                        endString=endString,
                        scoreint=scoreint -8,
                        indel=True)
            if ans3:
                consider.append(ans3)
            ans4 = score(
                        startString=startString,
                        endString=endString[1::],
                        scoreint=scoreint - 8,
                        indel=True)
            if ans4:
                consider.append(ans4)
            ans5 = score(
                        startString=startString[1::],
                        endString=endString[1::],
                        scoreint=scoreint - 3,
                        indel=False
                        )
            if ans5:
                consider.append(ans5)
            scoreint = max(consider)
        return (scoreint)


if __name__ == "__main__":
    with open(sys.argv[1], "rt") as file:
        lines = file.read().split("\n")
        for line in lines:
            partA, partB = line.split("|")
            try:
                number = score(partA, partB)
                print(number)
            except Exception as e:
                print (line)
                print (e)


