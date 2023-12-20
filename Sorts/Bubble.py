#bubble sort
#Put the biggest at the end
#rinse and repeat
#if no swap happens, end!
#time: O(n2)
#space: O(1)



def bubble(arr):
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

#feels ugly but it works
