import sys
match = 3
mismatch = -3
     

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
    grid = [0,0]+list(startString)
    grid[0] = [0]+list(endString)
    grid[1][1] = [0, False]
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
              A = grid[j]
              B = grid[0][i]
              if (matchletter(A,B)):
                  grid[j][i]=[grid[j-1][i-1] + match, False]
              else:
                  grid[j][i] = calcCell(grid[j-1][i], grid[j][i-1], grid[j-1][i-1])
    return (grid[-1][-1])
                              


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
