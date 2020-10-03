# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    # Is there a difference between these two initialization techniques?
    
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    merged_arr = []

    # How do I loop over the two lists, comparing values at each position
    # sequentially?
    
    # ranges = range(len(arrA)), range(len(arrB))
    # for ptrA, ptrB in ranges:
    #     print(ptrA, ptrB)

    while ptrA <= len(arrA) and ptrB <= len(arrB):
        if arrA[ptrA] < arrB[ptrB]:
            merged_arr.append(arrA[ptrA])
            ptrA += 1
        elif arrB[ptrB] < arrA[ptrA]:
            merged_arr.append(arrB[ptrB])
            ptrB += 1

    


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[:int(len(arr)/2)])
        right = merge_sort(arr[int(len(arr)/2):])
        merge(left, right)


    return arr

merge_sort([4,3,2,1])

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

