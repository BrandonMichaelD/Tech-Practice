
##Merge Sort!
##Divide, then sort while merge!
##Time: O(nLog(n))
##Space: O(n)

##Linked lists are great for merge

import randList

initial = randList.listCreate(40)

print("start")
print(initial)
print("-------------------------------------------------")


def merge(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge(left)
        merge(right)

        ii = 0
        jj = 0
        kk =0

        while ii < len(left) and jj < len(right):
            if left[ii] <= right[jj]:
                arr[kk] =left[ii]
                ii+=1
            else:
                arr[kk] = right[jj]
                jj+=1
            kk+=1
        
        while ii < len(left):
            arr[kk] = left[ii]
            ii +=1
            kk+=1
        while jj < len(right):
            arr[kk] = right[jj]
            jj +=1
            kk+=1

    

merge(initial)
print(initial)