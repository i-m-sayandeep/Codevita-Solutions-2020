from itertools import combinations

n = int(input())
arr = list(map(int,input().split()[:n]))
arr=sorted(arr,reverse=True)
arr1 =[]
arr1.append(bin(arr[0]).replace("0b",""))
for i in range(1,len(arr)):
    x = bin(arr[i]).replace("0b","")
    if(len(x) != len(arr1[0])):     
        b = len(arr1[0])-len(x)
        x = ("0"*b)+x
        arr1.append(x)
    else:
        arr1.append(x)

l=[]
for i in range(n):
    l.append(list(combinations(arr1,(i+1))))
count=0

for i in l:
    for j in i:
        s=""
        for k in j:
            s = s+k
            
        if(s.count("0")==s.count("1")):
            count+=1

c = bin(count).replace("0b","")
g = ("0" * (len(arr1[0])-len(c)))+c
print(g)