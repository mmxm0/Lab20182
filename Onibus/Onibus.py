def DFS(rotasCidades, origem, destino, pai, controle):
    if origem == destino:
        print(controle)
        return

    for pivo in rotasCidades[origem]:
        if pivo != pai:
            DFS(rotasCidades, pivo, destino,origem,controle+1)

ent = input().split()
rotasCidades = {}
for b in range(int(ent[0])):
    rotasCidades[b+1] = []

for c in range(int(ent[0])-1):
    t = input().split()
    rotasCidades[int(t[0])].append(int(t[1]))
    rotasCidades[int(t[1])].append(int(t[0]))

DFS(rotasCidades, int(ent[1]), int(ent[2]), None, 0)