def calcMin(tupla):
    if tupla[0] == tupla[1]:
        s = tupla[0]
    elif tupla[0] != tupla[1]:
        if tupla[0] > tupla[1]:
            s = tupla[1]
        else:
            s = tupla[0]
    return s

N = int(input())
pares = []
botasListagem = {}
for n in range(N):
    e = input().split()
    pares.append((int(e[0]), e[1]))
    try:
        if e[1] == "D":
            botasListagem[int(e[0])][0]+=1
        elif e[1] == "E":
            botasListagem[int(e[0])][1]+=1
    except KeyError:
        if e[1] == "D":
            botasListagem[int(e[0])]=[1, 0]
        elif e[1] == "E":
            botasListagem[int(e[0])]=[0, 1]
saida = 0

for b in botasListagem:
    tupla = (botasListagem[b][0], botasListagem[b][1])
    saida += calcMin(tupla)

print(saida)
