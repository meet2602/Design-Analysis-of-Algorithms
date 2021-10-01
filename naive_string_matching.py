'''
A research scholar submitted his/her work to deparment. Department 
wants to know that his/her report contents are original (not copy from 
someone). Write an algorithm to find whether the report is original or 
copied from some one
'''


def naive_string_matching(p, t):
    M = len(p)
    N = len(t)
    for i in range(0, N-M+1):
        d = 0
        for j in range(0, M):
            if t[i+j] != p[j]:
                break
            d = j+1
        if d == M:
            print("index", i)


# p = "AABA"
# t = "AABAACAADAABAAABAA"
t = input("Enter the text:")
p = input("Enter the pattern:")
naive_string_matching(p, t)
