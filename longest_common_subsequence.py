"""
In biological applications, we often want to compare the DNA of two 
(or more) different organisms. For example, the DNA of one organism may 
be S1 = ACCGGTCGAGTG while the DNA of another organism may be 
S2 = GTCGTTCGGAAT. One goal of comparing two strands of DNA is to 
determine how “similar” the two strands are, as some measure of how 
closely related the two organisms are.
"""
x = "ACCGGTCGAGTG"
y = "GTCGTTCGGAAT"

#x = "ABAZDC"
#y = "BACBAD"

print("X = "+str([i for i in x]))
print("Y = "+str([i for i in y]))
m, n = len(x), len(y)
b = [[0 for j in range(n+1)] for i in range(m+1)]
c = [[0 for j in range(n+1)] for i in range(m+1)]
mat = [[0 for j in range(n+1)] for i in range(m+1)]


def lcs_length(x, y):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = (c[i-1][j-1]) + 1
                b[i][j] = u'\u2196'

            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = u'\u2191'

            else:
                c[i][j] = c[i][j-1]
                b[i][j] = u'\u2190'
            mat[i][j] = str(c[i][j]) + str(b[i][j])

    ls = []
    for i in range(0, len(mat)):
        ls.append(list(mat[i]))

    for i in ls:
        if ls.index(i) == 0:
            print("xi"+str(i))
        else:
            print(str(x[ls.index(i)-1])+str(i))

    print("\nc[m,n] = ", c[m-1][n])


# lcs_length("ABAZDC", "BACBAD")

lcs_length(x, y)


def print_LCS(b, x, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == u'\u2196':
        print_LCS(b, x, i-1, j-1)
        print(x[i])
    elif b[i][j] == u'\u2191':
        print_LCS(b, x, i-1, j)
    else:
        print_LCS(b, x, i, j-1)


print_LCS(b, "0"+x, len(x)-1, len(y))
