#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(mat):

    s=-64
    maxi=-64
    
        
    for x in range(4):
        for y in range(4):
            s= mat[x][y]+mat[x][y+1]+mat[x][y+2]+mat[x+1][y+1]+mat[x+2][y]+mat[x+2][y+1]+mat[x+2][y+2]
            print(s)
            if s>maxi:
                maxi=s

    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mat = []

    for _ in range(6):
        mat.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(mat)

    fptr.write(str(result) + '\n')

    fptr.close()
