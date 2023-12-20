import randList
import Counting

from timeit import default_timer

initial = randList.listCreate(200000)
initial2 = initial
start1 = default_timer()

Counting.countingSort(initial)

duration1 = default_timer() - start1
print(duration1)
print('VS')
start2 = default_timer()

Counting.countingInPlace(initial2)

duration2 = default_timer()-start2

print(duration2)