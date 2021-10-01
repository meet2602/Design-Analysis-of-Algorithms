"""
Suppose you are having a set of trump cards, each card is having one 
letter on it. To play a game it would be better if all the trump cards will be 
arranged. To arrange trump cards following technique should be adopted.
Take very first card as a Key element and try to place it on its final position 
of arrangement. Repeat this procedure until all the cards will be arranged.
Card No 1 2 3 4 5 6 7
Value D W A S E U G
"""
import time
import random


def insertion_sort(array):
    for step in range(2, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


try:
    len_list = int(input("Enter no of Card:"))
    if len_list < 0:
        print("Sorry,negative size")
    else:
        card_list = []
        for i in range(len_list):
            k = input("Enter card "+str(i+1)+" value: ")
            card_list.append(k)
        s = time.time()
        print("unorder card value list is: ", card_list)
        print("sorted  card value list is: ", insertion_sort(card_list))
        e = time.time()
        print("Exeution time", e-s)
except ValueError:
    print('Please input a valid integer')


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
