# Implement bubble sort algorithm and measure its execution time
import time
import random


def bubble_sort(student_list):
    for i in range(0, len(student_list)-1):
        for j in range(len(student_list)-i-1):
            if(student_list[j] > student_list[j+1]):
                student_list[j], student_list[j +
                                              1] = student_list[j+1], student_list[j]
    return student_list


# best case
student_list = [i for i in range(10000)]
print("Best Case")
s = time.time()
bubble_sort(student_list)
e = time.time()
print("Exeution time", e-s)
print()

# Worst case
print("Worst Case")
student_list = [i for i in range(10000, -1, -1)]
s = time.time()
bubble_sort(student_list)
e = time.time()
print("Exeution time", e-s)
print()

# Average case
print("Average Case")
student_list = [random.randint(0, 100000) for i in range(10000)]
s = time.time()
bubble_sort(student_list)
e = time.time()
print("Exeution time", e-s)
print()


# try:
#     len_list = int(input("Enter no of student:"))
#     if len_list < 0:
#         print("Sorry,negative size")
#     else:
#         student_list = []
#         for i in range(len_list):
#             k = int(input("Enter student id "+str(i+1)+" height: "))
#             student_list.append(k)
#         s = time.time()
#         print("unorder student height list is: ", student_list)
#         print("sorted  student height list is: ", bubble_sort(student_list))
#         e = time.time()
#         print("Exeution time", e-s)
# except ValueError:
#     print('Please input a valid integer')
