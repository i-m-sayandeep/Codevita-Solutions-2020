def U(x,y):
    if(x[0][y:y+3].count("*")==2):
        return True
    return False

def A(x,y):
    if(x[0][y:y+3].count("*")==1):
        return True
    return False

def selectLetter(a,b):
    if(a[1][i:i+3].count("*")==1):
        return("I")
    elif(a[1][i:i+3].count("*")==2):
        if(U(a,i)):
            return("U")
        else:
            return("O")
    else:
        if(A(a,i)):
            return("A")
        else:
            return("E")



n = int(input())
arr=[]
for i in range(3):
    arr.append(list(map(str,input().split()[:n])))

output=""
i=0
while(i<n):
    if(arr[2][i]=="#"):
        output+="#"
        i+=1
    elif(arr[2][i]=="*"):
        a = selectLetter(arr,i)
        output+=a
        i+=3
    else:
        i+=1

print(output)