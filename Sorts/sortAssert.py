'''
Assert that the list is sorted!
'''

def check(arr):
    for ii in range(1,len(arr)):
        assert arr[ii] >= arr[ii-1], f"order incorrect between index {ii-1} and {ii}"
    print("It's sorted!")