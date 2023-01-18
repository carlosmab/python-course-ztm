# debugging pdb
import pdb

def add(num1, num2):
    pdb.set_trace()
    num1 = num1 * 2
    num2 = num2 * 5
    return num1 + num2

add(4, 5)


## shows step by step in console