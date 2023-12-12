#A function to create random lists of (num) integers
import random
random.seed()

def listCreate(num):
    dataList = []
    for ii in range(num):
        dataList.append(random.randint(0,999))
    return dataList
