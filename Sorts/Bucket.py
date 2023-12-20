##Bucket sort!
##First, split into buckets based on range!
##Second, run a sort on each bucket
##Third, merge into the final array!


import QuickTwo

##make the list
#initial = randList.listCreate(500)

#print("start")
#print(initial)
#print("-------------------------------------------------")

##randList is 0 to 999 so we can divide by 100

def bucketSort(arr):
    buckets = [-1]*10 
    for num in arr: #writing it out for clarity
        index = num//100
        if buckets[index] == -1:
            buckets[index] = [num]
        else:
            buckets[index].append(num)
    ##buckets made!
    arr.clear()
    for bucket in buckets:
        if bucket != -1:
            QuickTwo.quickSort(bucket,0,len(bucket)-1)
            ##quickTwo sorts in place
            arr += bucket
