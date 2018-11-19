N = int(input())
botas = {}
botasIndex =[]
while N>0:
    e = input().split()
    try:

        if e[1] =="D":
            botas[e[0]][0]+=1
        elif e[1] =="E":
            botas[e[0]][1]+=1
    except:
        if e[1] == "D":
            botas[e[0]][0] = 1
        else:
            botas[e[0]][1] = 1

    if e[0] not in botasIndex:
        botasIndex.append(e[0])
    N-=1
print(botas)
print(botasIndex)