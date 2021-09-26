import time
import random


def insertion_sort(array):
    for step in range(2, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:

            array[j + 1] = array[j]
            j = j - 1
            print("j = ", j)

        print("i = ", step)
        array[j + 1] = key
        print(array)
    return array


# # best case
# card_list = [i for i in range(10000)]
# print("Best Case")
# s = time.time()
# insertion_sort(card_list)
# e = time.time()
# print("Exeution time", e-s)
# print()

# # Worst case
# print("Worst Case")
# card_list = [i for i in range(10000, -1, -1)]
# s = time.time()
# insertion_sort(card_list)
# e = time.time()
# print("Exeution time", e-s)
# print()


# # average case
# print("Average Case")
# card_list = [random.randint(0, 100000) for i in range(10000)]
# s = time.time()
# insertion_sort(card_list)
# e = time.time()
# print("Exeution time", e-s)
# print()


# try:
#     len_list = int(input("Enter no of Card:"))
#     if len_list < 0:
#         print("Sorry,negative size")
#     else:
#         card_list = []
#         for i in range(len_list):
#             k = input("Enter card "+str(i+1)+" value: ")
#             card_list.append(k)
#         s = time.time()
#         print("unorder card value list is: ", card_list)
#         print("sorted  card value list is: ", insertion_sort(card_list))
#         e = time.time()
#         print("Exeution time", e-s)
# except ValueError:
#     print('Please input a valid integer')
card_list = [5, 1, 12, -5, 16, 2, 12, 14]
print("unorder card value list is: ", card_list)
print("sorted  card value list is: ", insertion_sort(card_list))
