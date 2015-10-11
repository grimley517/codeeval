#! usr/bin/env python3

import sys


def reccount(stringIn, startindex=0, ans=0):
    stringtest = stringIn[startindex:]
    if len(stringtest) < 2:
        return(ans)
    elif int(stringtest[0:1]) < 27:
        ans += reccount(stringtest, startindex=2, ans=0) + 1
    return (reccount(stringtest, startindex=1, ans=ans))


def main(numinput):
    strinput = str(numinput)
    answer = reccount(strinput, startindex = 0, ans = 0)+1
    return (answer)

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        for line in file.readlines():
            line = line.strip()
            print(line, ' -> ', main(line))
