#!/bin/python3

import math
import os
import random
import re
import sys

def quartiles2(arr):
    
    arr = sorted(arr)
    siz = len(arr)
    
    if siz%2 >0:
        Q = arr[siz // 2]
        arrInf = arr[:siz // 2]
        arrSup = arr[(siz // 2)+1:]

        if (len(arrInf)%2>0):
            Q2 = arrInf[len(arrInf) // 2]
            Q3 = arrSup[len(arrSup) // 2]
        else:
            Q2 = (arrInf[len(arrInf)// 2] + arrInf[len(arrInf) // 2 - 1 ])/2
            Q3 = (arrSup[len(arrSup)// 2] + arrSup[len(arrSup) // 2 - 1 ])/2

        return [ Q2, Q , Q3]

    else:
        Q = (arr[siz// 2] + arr[siz // 2 - 1 ])/2
        arrInf = arr[:(siz // 2)]
        arrSup = arr[(siz // 2):]

        if (len(arrInf)%2>0):
            Q2 = arrInf[len(arrInf) // 2]
            Q3 = arrSup[len(arrSup) // 2]
        else:
            Q2 = (arrInf[len(arrInf)// 2] + arrInf[len(arrInf) // 2 - 1 ])/2
            Q3 = (arrSup[len(arrSup)// 2] + arrSup[len(arrSup) // 2 - 1 ])/2
       
        return [ Q2, Q , Q3]  


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

#2
#19
#59 60 65 65 68 69 70 72 75 75 76 77 81 82 84 87 90 95 98
#Quartile 1 (Q1) = 68. Quartile 2 (Q2) = 75 Quartile 2 (Q3) = 84

#3
#10
#1 3 3 4 5 6 6 7 8 8
#Quartile 1 (Q1) = 3. Quartile 2 (Q2) = 5.5.