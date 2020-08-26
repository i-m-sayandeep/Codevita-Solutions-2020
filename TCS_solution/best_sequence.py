from itertools import permutations
def keyCombo(x):
    y =list(permutations(x))
    a=[]
    for i in y:
        a.append("".join(i))
    return(a)    


s = input()
y = list(map(str,input().split()))
keys = "".join(y)
combo = keyCombo(keys)
combo = sorted(combo)
l=[]
for i in combo:
    l.append(s.count(i))
a = l.index(max(l))
print(combo[a])