#!/bin/python3

import math
import os
import random
import re
import sys

def quartiles(arr):
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

        return [ int(Q2), int(Q) , int(Q3)]

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
       
        return [ int(Q2), int(Q) , int(Q3)]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
