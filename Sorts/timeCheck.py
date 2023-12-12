import randList
import Bucket
import BucketPostman

from timeit import default_timer

initial = randList.listCreate(10000)
initial2 = initial
start1 = default_timer()

Bucket.bucketSort(initial)

duration1 = default_timer() - start1
print(duration1)
print('VS')
start2 = default_timer()

BucketPostman.postmanBucket(initial2)

duration2 = default_timer()-start2

print(duration2)