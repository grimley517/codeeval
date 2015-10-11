import sys

''' From  a file entered as an input item  converts each line from a hex integer to a decimal based integer, and prints the decimal integer'''
def matchLetter(letterA, letterB):
    if (letterA == letterB):
        return (True)
    else:
        return (False)

def score(startString, endString, index1=0, index2=0, scoreint =0, indel= False):
    if(index1< len(startString) and index2<len(endString)):
        if index1 >=len(startString):
            index1 = len(startString)-1
            if (indel):
                scoreint -= 1
            else:
                scoreint -=8
                indel = True
        if index2 >= len(endString):
            index2 = len(endString)-1
            if (indel):
                scoreint -= 1
            else:
                scoreint -=8
                indel = True
        if matchLetter(startString[index1], endString[index2]):
            scoreint = score(
                            startString = startString,
                            endString = endString,
                            index1 = index1 +1,
                            index2 = index2 +1,
                            scoreint = scoreint +3,
                            indel = False)
        elif(indel):
            ans1 = score(
                        startString = startString,
                        endString = endString,
                        index1 = index1 +1,
                        index2 = index2,
                        scoreint = scoreint -1,
                        indel = True)
            ans2 = score(
                        startString = startString,
                        endString = endString,
                        index1 = index1,
                        index2 = index2 +1,
                        scoreint = scoreint -1,
                        indel = True)
            ans5 = score(
                        startString = startString,
                        endString = endString,
                        index1 = index1 +1,
                        index2 = index2 +1,
                        scoreint = scoreint -3,
                        indel = False)
            scoreint = max(ans1, ans2, ans5)
        else:
            ans3 = score(
                        startString = startString,
                        endString = endString,
                        index1 = index1 +1,
                        index2 = index2,
                        scoreint = scoreint -8,
                        indel = True)
            ans4 = score(
                        startString = startString,
                        endString = endString,
                        index1 = index1,
                        index2 = index2 +1,
                        scoreint = scoreint -8,
                        indel = True)
            ans5 = score(
                        startString = startString,
                        endString = endString,
                        index1 = index1 +1,
                        index2 = index2 +1,
                        scoreint = scoreint -3,
                        indel = False)
            scoreint = max(ans3, ans4, ans5)
    else:
        return (scoreint)

if __name__ == "__main__":
    with open (sys.argv[1],"rt") as file:
        lines = file.read().split("|")
        for line in lines:
            try:
                number = score(line)
                print(number)
            except e as Exception:
                print (line)
                print (e)

    input()
