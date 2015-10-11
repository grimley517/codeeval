import sys
with open(sys.argv[1],'r')as tnums:
    tnums = tnums.read()
    tnums = tnums.split('\n')
    for tnum in tnums:
        tnum = tnum.strip()
        answer = True
        for letter in tnum:
            if tnum.count(str(tnum.index(letter)))!=int(letter):
                answer = False
print (int(answer))
