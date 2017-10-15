import random as rd
from time import clock
import sys

arr = [rd.randint(1,897) for i in range(12)]

def qsort(arr):
    if not arr: return arr
    left = [i for i in arr[1:] if i<=arr[0]]
    right = [i for i in arr[1:] if i>arr[0]]
    return qsort(left)+[arr[0]]+qsort(right)

def insertion(arr):
    n = len(arr)
    for i in range(n):
        ind = i
        for j in range(i,n):
            if arr[j]<arr[ind]:
                ind = j
        arr[i],arr[ind] = arr[ind],arr[i]
    return arr

def msort(arr):
    if not arr: return arr
    n = len(arr)//2
    left = msort(arr[:n])
    right = msort(arr[n:])
    li,ri=0,0
    ans = []
    for i in range(len(arr)):
        if left[li]<=right[ri]:
            ans.append(left[li])
            li+=1
        else:
            ans.append(left[li])
            ri+=1
        if li==len(left):
            ans+=right[ri:]
            break
        if ri==len(right):
            ans+=left[li:]
            break
    return ans

def call(func,arg):
    x = clock()
    t=func(arg)
    print(clock()-x)

def test(func,n=5):
    for i in range(n):
        arr = [rd.randint(1,897) for i in range(12)]
        print(sorted(arr)==func(arr))







