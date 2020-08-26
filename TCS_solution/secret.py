from collections import Counter

s = input()
n = int(input())
l=dict()
for i in range(n):
    a,b = map(str,input().split())
    x = Counter(a)
    y = Counter(b)
    z = x.keys()
    