##Bucket sort but I wanted to try Postman's algorithm
##First we make buckets to split by FIRST signigificant figure
##Then we check the elements in bucket by the SECOND sig figure
##Then when we put it back together, we check by the THIRD

import randList
import sortAssert


#initial = randList.listCreate(500)

#print("start")
#print(initial)
#print("-------------------------------------------------")

def stringConvert(number): #a function to make every string 3 digits
    if number >99:
        return str(number)
    elif number >9:
        return "0"+str(number)
    else:
        return "00"+str(number)


def postmanBucket(arr):
    ##randList is only three significant digits so only 10 buckets
    buckets = [[None] for i in range(10)]
    for num in arr: ##writing it out for clarity
        index = num //100
        if buckets[index]== [None]:
            buckets[index] = [num]
        else:
            strNum = stringConvert(num)
            insert = False
            for element in buckets[index]:
                strElement = stringConvert(element)
                if strElement[1]>= strNum[1]:
                    newIndex = buckets[index].index(element)
                    buckets[index].insert(newIndex,num)
                    insert = True
                    break

            if insert ==False:
                buckets[index].append(num)
    
   
    ##Buckets are READY
    arr.clear()
    arrIndex = 0
    for bucket in buckets:
        arr.append(bucket[0])
        arrIndex+=1
        for ii in range(1,len(bucket)):
            checkIndex = arrIndex
            while bucket[ii] < arr[checkIndex-1]:
                checkIndex -=1
                if checkIndex<1:
                    break
            arr.insert(checkIndex,bucket[ii])
            arrIndex+=1


##I think I did an ok job implementing this in a READABLE way, but I'm not sold that it would be faster than bucket sort as is.
##Maybe if we separated integer checks to run parallel? idk.
"""
SO I checked the times using timeIt and on the same random list of 10000 integers
bucketSort using quickSort:
0.015188700053840876
VS
bucketSort checking integers in THIS PARTICULAR implementation:
0.7802065000287257

I'd sooner believe theres an issue with my implementation than anything else, but my gut instinct was right.

"""

##Ok I did some more research
##This isn't actually postman's
##In postman sort the keys are NOT compared.
##Implementation maybe through dictionaries so only the individual digits are paid attention to?
##Or maybe recursive by digit by bucket all the way down?
##I'm not sure but honestly I don't think a random list of integers is the optimal use for this sort
##Maybe hexadecimal strings of characters?
##Or maybe hecking long numbers?
