'''
You are given n activities with their start and finish times. Select the 
maximum number of activities that can be performed by a single 
person, assuming that a person can only work on a single activity at a 
time.
'''


def greedy_activity_selector(s, f):
    n = len(s)
    A = [1]
    k = 0
    for m in range(0, n):
        if s[m] >= f[k]:
            A.append(m+1)
            k = m

    print(A)


s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
greedy_activity_selector(s, f)
