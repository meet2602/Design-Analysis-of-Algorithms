"""
Creates two empty arrays to hold elements less than the pivot value 
and elements greater than the pivot value, and then recursively sort the sub 
arrays. There are two basic operations in the algorithm, swapping items in 
place and partitioning a section of the array.
"""
import time
import random
a = [5, 4, 2, 51, 48, 31, 52]


def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= x:
            i = i+1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def quickSort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quickSort(a, p, q-1)
        quickSort(a, q+1, r)


s = time.time()
print("unorder list is: ", a)
quickSort(a, 0, len(a)-1)
print("sorted  list is: ", a)
e = time.time()
print("Exeution time", e-s)


# # best case
# card_list = [i for i in range(100)]
# print("Best Case")
# s = time.time()
# quickSort(card_list, 0, len(card_list)-1)
# e = time.time()
# print("Exeution time", e-s)
# print()

# # Worst case
# print("Worst Case")
# card_list = [i for i in range(100, -1, -1)]
# s = time.time()
# quickSort(card_list, 0, len(card_list)-1)
# e = time.time()
# print("Exeution time", e-s)
# print()


# # average case
# print("Average Case")
# card_list = [random.randint(0, 999) for i in range(100)]
# s = time.time()
# quickSort(card_list, 0, len(card_list)-1)
# e = time.time()
# print("Exeution time", e-s)
# print()
