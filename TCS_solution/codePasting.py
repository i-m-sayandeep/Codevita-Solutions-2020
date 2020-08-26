from itertools import permutations
def minsubset(arr,n,val):
    mat = [[False for i in range(val+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(val+1):
            if(i==0):
                mat[i][j]=False
            if(j==0):
                mat[i][j]=True

    for i in range(1,n+1):
        for j in range(1,val+1):
            if(arr[i-1]<=j):
                mat[i][j]=mat[i-1][j-arr[i-1]] or mat[i-1][j]
            else:
                mat[i][j]= mat[i-1][j]

    vector=[]
    for i in range((val+1)//2):
        if(mat[n][i]):
            vector.append(i)

    return vector

x = list(permutations("su"))
a=[]
for i in x:
    a.append("".join(i))
a.extend(["s","u"])
s = "supreme court is the highest judicial court"
y=[] 
for i in a:
    y.append(s.count(i))
print(y)
n=len(y)
val = sum(y)
b = minsubset(y,n,val)
print(val-(max(b)))
