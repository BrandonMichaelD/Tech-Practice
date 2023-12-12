##Heap sort!
##First we take an array and turn it into a max heap (heapify)
##->an array that if created into a binary tree in order, would be a max heap
## Then one by one swap the largest(first) element with the smallest(last)
##Remove the last and repeat => sorted array!
##To keep the sort in place, N is the number of elements
import randList
import sortAssert

initial = randList.listCreate(10000)

def heapify(arr,index, N):
    max = index  #index of the max value
    leftLeaf = index * 2 +1
    rightLeaf = index * 2 +2

    if leftLeaf < N and arr[leftLeaf] > arr[max]:
        max = leftLeaf

    if rightLeaf < N and arr[rightLeaf] > arr[max]:
        max = rightLeaf
    
    ##Swap!
    if max != index:
        arr[index], arr[max] = arr[max], arr[index]

        #recursion!
        heapify(arr, max, N)




def heap(arr,N):
    startInd = len(arr)//2-1

    for ii in range(startInd,-1,-1):  #count backwards
        heapify(arr,ii,N)


def heapSort(arr):
    heap(arr,len(arr))

    for ii in range(len(arr)-1,-1,-1):
        arr[ii], arr[0] = arr[0], arr[ii] #Swap smallest(last) with largest(first)
        heapify(arr,0,ii)


heapSort(initial)
sortAssert.check(initial)