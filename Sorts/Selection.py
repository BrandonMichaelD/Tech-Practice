#Selection sort! A classic!
#Go down the list, find the smallest, put it in its spot


def selectionSort(arr):
    index = 0
    while index < len(arr):
        bookmark = index
        for ii in range(index,len(arr)):
            if arr[ii] < arr[bookmark]:
                bookmark = ii
            
        #we're through the list
        #swap smallest with index
        if bookmark!= index: 
            arr[bookmark],arr[index] = arr[index],arr[bookmark] #no swap if not different
        index+=1
        

)