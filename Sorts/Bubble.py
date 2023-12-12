#bubble sort
#Put the biggest at the end
#rinse and repeat
#if no swap happens, end!
#time: O(n2)
#space: O(1)

initial = [7,2,1,8,43,1,6,4,3,22,1,6,7]


for ii in range(len(initial)):

    swapped = False
    for jj in range(len(initial)):
        if initial[ii] < initial[jj]:
            temp = initial[jj]
            initial[jj] = initial[ii]
            initial[ii] = temp
            swapped = True
    if swapped == False:
        break
print(initial)

#feels ugly but it works
