## Trying to optimize quickSort
##First: random pivots
##Bonus: fewer swaps!
##Con: more checks (those if's and's)
##Time: O(nlog(n)), random helps avoid O(n2)
##Space: O(log(n)) because of that recursion stack


import random
import randList

"""initial = randList.listCreate(500)

print("start")
print(initial)
print("-------------------------------------------------")
"""



def partition(arr,start,end):
    pivotInd = random.randint(start,end)
    pivot = arr[pivotInd]
    #pointer from each end

    high = end
    low = start
    #we dont know where pivot is
    while low < high:
        while arr[low] <= pivot and pivotInd > low:
            #leave it alone, it doesnt need to be moved
            low+=1
        #we now have the last of <= pivot
        if pivotInd != low:
            arr[low],arr[pivotInd] = arr[pivotInd],arr[low]
            pivotInd=low
        while arr[high] > pivot and pivotInd<high:
            #leave it alone, it doesn't need to be moved
            high -=1
        #we now have a <= pivot  
        if pivotInd != high:
            arr[high],arr[pivotInd] = arr[pivotInd],arr[high]
            pivotInd = high
    return pivotInd



def quickSort(arr,start,end):
    if start < end:

        pivot = partition(arr, start,end)
        quickSort(arr, start,pivot-1) #left
        quickSort(arr,pivot+1,end) #right
    

