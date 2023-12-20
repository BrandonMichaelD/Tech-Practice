#Insertion Sort!
"""
Iterate over the array and compare key to key-1
If key smaller than key-1, move other elements up to make space
Time: O(n2)
Space: O(1)


"""

def sort(arr):
    for ii in range(1,len(arr)): #start at the second index
        if arr[ii] < arr[ii-1]:
            temp = arr[ii]
            index = ii
            while temp <= arr[index-1] and index >0:
                arr[index] = arr[index-1]
                index -= 1
            
            arr[index] = temp

