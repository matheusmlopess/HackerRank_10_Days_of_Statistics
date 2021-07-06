#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile2(values, freqs):
    
    
    arr = [ values[i] for i,fd in enumerate(freqs, 0) for c in range(fd)]
    siz = len(arr)
    arr = sorted(arr)
   
    if siz%2 >0:
        Q = arr[siz // 2]
        arrInf = arr[:siz // 2]
        arrSup = arr[(siz // 2)+1:]

        if (len(arrInf)%2>0):
            Q1 = arrInf[len(arrInf) // 2]
            Q3 = arrSup[len(arrSup) // 2]

        else:
            Q1 = (arrInf[len(arrInf)// 2] + arrInf[len(arrInf) // 2 - 1 ])/2
            Q3 = (arrSup[len(arrSup)// 2] + arrSup[len(arrSup) // 2 - 1 ])/2

        fin = round(float(Q3 - Q1),1)
        print(fin) 
        #return [ int(Q1), int(Q) , int(Q3)]

    else:
        Q = (arr[siz// 2] + arr[siz // 2 - 1 ])/2
        arrInf = arr[:(siz // 2)]
        arrSup = arr[(siz // 2):]

        if (len(arrInf)%2>0):
            Q1 = arrInf[len(arrInf) // 2]
            Q3 = arrSup[len(arrSup) // 2]

        else:
            Q1 = (arrInf[len(arrInf)// 2] + arrInf[len(arrInf) // 2 - 1 ])/2
            Q3 = (arrSup[len(arrSup)// 2] + arrSup[len(arrSup) // 2 - 1 ])/2

        fin = round(float(Q3 - Q1),1)
        print(fin) 
        #return [ int(Q1), int(Q) , int(Q3)]


    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
    
    
