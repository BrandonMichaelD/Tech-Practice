#Insertion Sort!
"""
Iterate over the array and compare key to key-1
If key smaller than key-1, move other elements up to make space
Time: O(n2)
Space: O(1)


"""
import randList
initial = randList.listCreate(40)
print(initial)


for ii in range(1,len(initial)): #start at the second index
    if initial[ii] < initial[ii-1]:
        temp = initial[ii]
        index = ii-1
        while temp <= initial[index] and index >0:
            initial[index+1] =initial[index]
            index -=1
        initial[index] = temp

print(initial)