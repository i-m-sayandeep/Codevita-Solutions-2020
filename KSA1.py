# def count(arr,n,b):
#     dp  = [[-1 for i in range(b+1)]for j in range(n+1)]

#     for i in range(n+1):
#         for j in range(b+1):
#             if(i==0):
#                 dp[i][j]=0
#             if(j==0):
#                 dp[i][j]=1

#     for i in range(1,n+1):
#         for j in range(1,b+1):
#             if(arr[i-1]<=j):
#                 dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i-1][j]
    
#     return(dp[n][b])
def count(arr,n,b):
    arr = sorted(arr)
    val = 0
    cou = 0
    for i in range(n):
        val+=arr[i]
        if(val<=b):
            cou +=1
        else:
            break
    return(cou)

for i in range(int(input())):
    n, b = map(int,input().split())
    arr = list(map(int,input().split()[:n]))
    x = count(arr,n,b)
    print("Case #{}: {}".format(i+1,x))