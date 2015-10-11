import sys

''' From  a file entered as an input item  converts each line from a hex integer to a decimal based integer, and prints the decimal integer'''

def dec(hexString):
    '''Takes a string representation of a hexadecimal number and converts it into a decimal integer'''
    number = int(hexString, base=16)
    return (number)

if __name__ == "__main__":
    with open (sys.argv[1],"rt") as file:
        lines = file.read().split("\n")
        for line in lines:
            try:
                number = dec(line)
                print(number)
            except:
                pass
