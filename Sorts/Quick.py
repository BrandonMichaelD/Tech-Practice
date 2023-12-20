##QuickSort!
##Pick a key
##Partition around that key


##This is brute slowest QuickSort
##Pivot is always end
##Smells weird






def partition(arr,start,end):
    pivot = arr[end]
    #pointer to cycle through

    low = start-1

    for ii in range(start,end):
        if arr[ii]<=pivot:
            #swap with low pointer
            low+=1
            arr[low],arr[ii] = arr[ii],arr[low]
    #loop done, swap pivot
    low+=1
    arr[low],arr[end] = arr[end],arr[low]
    return low

def quickSort(arr,start,end):
    if start < end:

        pivot = partition(arr, start,end)
        quickSort(arr, start,pivot-1) #left
        quickSort(arr,pivot+1,end) #right
    



##I also found this implementation while still likely n^2 run time (pivot is first element)
##I think it's elegant
'''
def quickSort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        left = [i for i in arr[1:] if i < pivot]
        right = [i for i in arr[1:] if i >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)
    else:
        return arr


'''