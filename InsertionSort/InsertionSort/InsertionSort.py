from random import *

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def RandomArr(kol,_seed):
    seed(_seed)
    A=[randint(0,50) for _ in range(kol)]
    return A

A=[]
A=RandomArr(15,5)
print(A)
#print(insertion_sort(A))