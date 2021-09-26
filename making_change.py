def Coins(N, d):
    c = [[] for i in range(len(d))]
    for i in range(len(d)):
        for j in range(N+1):
            c[i].append(0)
    for i in range(1, len(d)):
        c[i][0] = 0

    for i in range(len(d)):
        for j in range(1, N+1):
            if i == 0 and j < d[i]:
                c[i][j] = 99
            elif i == 0:
                c[i][j] = 1+c[i][j-d[i]]
            elif j < d[i]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = min((c[i-1][j]), (1+c[i][j-d[i]]))
    # for i in range(len(c)):
    #     print(c[i])
    print("\nTotal coins:"+str(c[len(d)-1][N])+"\n")


try:
    N = int(input("N:"))
    len_list = int(input("Enter no of n:"))
    if len_list < 0:
        print("Sorry,negative size")
    else:
        d = []
        for i in range(0, len_list):
            k = int(input("Enter n"+str(i+1)+": "))
            d.append(k)
        print("n = ", d)
        Coins(N, d)
except ValueError:
    print('Please input a valid integer')
