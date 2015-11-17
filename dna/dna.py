import sys
match = 3
mismatch = -3
grid = [[]]
     
'''https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm'''
def matchLetter(letterA, letterB):
    return (letterA == letterB)

def indelscore(indelstate):
    if indelstate:
        return -1
    else:
        return -8

def clean(instring):
    allowed = "ACGT"
    answer = ""
    instring = instring.upper()
    for letter in instring:
        if letter in allowed:
            answer += letter
    return (answer)

def missmatch (cell):
    score = cell[0] +mismatch
    return(score)

def indel(cell):
    ongoing = cell[1]
    score = cell[0] + indelscore(cell[1])
    return(score)

def calcCell(up, left, diag):
     maxindel = max(indel(up),indel(left))
     mmatch = missmatch(diag)
     if mmatch > maxindel:
         return([mmatch,False])
     else:
        return([maxindel,True])
     

def score(startString, endString):
    grid = [[0]]
    for letter in startString:
        grid.append([grid[-1][0]+missmatch])
    for letter in endString:
        grid[0].append(grid[0][-1]+missmatch)
    for y in range(1,len(grid[0]-1)):
        for x in range(1,len(grid)-1):
            if (startString[x-1] == endString[y-1]):
                grid[x][y] = grid[x-1][y-1]+match
            else:
                calcCell
                              


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
