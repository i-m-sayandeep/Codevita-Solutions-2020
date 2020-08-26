def countSubset(arr,n,val):
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
                
    return(mat[n][val])


arr=[1,3,2,4,2]
n = len(arr)
val = sum(arr)
x = countSubset(arr,n,val)
print(x,sum(arr)//2)