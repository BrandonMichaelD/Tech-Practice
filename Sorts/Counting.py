# Find the max element
#Initialize a countArray of max+1
#Count the elements!
#Run through the counts and make a cumulative sum for each index
#Iterate through input and finalize the array (from the end for stability)
#Im going to do two variations, the first is with an output array (good in case the elements have extra data)
#The other will be in place, to save on space, assuming the values are JUST values

def countingSort(arr):
    max = 0
    for element in arr: #Find Max
        if element > max:
            max = element
            
    countArray = [0]*(max+1) #CountArray!
    for element in arr:
        countArray[element]+=1
        
    for ii in range(1,len(countArray)):
        countArray[ii] += countArray[ii-1]
        
    
    outArray = [0] * len(arr)
    for ii in range(len(arr)-1,-1,-1): #going backwards
        #writing this out for readability

        element = arr[ii]
        outIndex = countArray[element]
        outArray[outIndex-1] = element
        countArray[element]-=1 #Decrement the index to fill in the spot before!
   
    
    #This is to match the in-place return of the other files in this repository
    arr.clear()
    arr.append(outArray)




def countingInPlace(arr):
    #This first part is the same
    max = 0
    for element in arr: #Find Max
        if element > max:
            max = element
                 
    countArray = [0]*(max+1) #CountArray!
    for element in arr:
        countArray[element]+=1
        
    #Now we have our countarray! So I'm going to iterate through it to change the original list
    index = 0
    for ii in range(len(countArray)):
        while countArray[ii] > 0:
            arr[index] = ii
            index+=1
            countArray[ii] -=1
         


"""
So I checked the times between the two (after disabling the array copy in countingSort to make it fair)
At 200,000 elements timeCheck returned these durations:
countingSort : 0.026550099999999993
VS
countingInPlace : 0.021628800000000004

The second is an improvement on time AND space
"""