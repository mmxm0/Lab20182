n = int(input())
total =10
l =[None]*n
for i in range(n):
    T = int(input())
    l[i]=T

for j in range(n-1):
    p1 = l[j]
    p2 = l[j+1]
    p = p1-p2
    if abs(p)>10: 
        total+=10
    else:
        total+=abs(p)
print(total)
