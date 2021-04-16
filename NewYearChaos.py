#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(arr):
    f=0
    swap=0

    for i in range(n):
        if arr[i]-1 > i:
            val= arr[i]-1-i
            #print(arr[i],"-1-",i,"=",val)
            if val > 2:
                f=1
                break

    if f==0:
        for i in range(n-2):
            for j in range(n-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1]= arr[j+1], arr[j]
                    swap+=1
            if sorted(arr) == arr:
                break
        return(swap)
    else:
        return("Too chaotic")

if __name__ == '__main__':
    t = int(input())
    ans=[]
    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        ans.append(minimumBribes(arr))
    for x in range(len(ans)):
        print(ans[x])
