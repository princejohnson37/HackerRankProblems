#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    d = {}
    for i in s:
        d[i] = 0
    for i in s:
        v = d[i]
        d[i] = v +1
    l = len(s)
    dict_len = len(d)
    count_even = 0
    count_odd = 0
    for i in d.keys():
        a = d[i]
        if(a%2==0):
            count_even+=1
        else:
            count_odd +=1
    print(d)
    print("even ",count_even)
    print("odd ",count_odd)
    if((l%2==0 and count_odd<1 and count_even>0) or (l%2!=0 and count_odd==1)) :
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
