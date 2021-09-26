n=5
W=11
w=[1,2,5,6,7]
v=[1,6,18,22,28]
c = [[0 for j in range(W+1)] for i in range(n)]
for i in range(len(c)): 
	print(c[i])
for i in range(0,n):
	c[i][0] = 0
for i in range (0,n) :
    for j in range (0,W+1) :
        if i == 0:
            if j < w[i]:
                c[i][j] = 0
            else:
                c[i][j] = v[i]
        elif j<w[i] :
            c[i][j] = c[i-1][j]
        else:
            c[i][j] = max(c[i-1][j],c[i-1][j-w[i]] + v[i])
print("table=")            
for i in range(len(c)): 
	print(c[i])
	
print("profit=",c[n-1][W])
