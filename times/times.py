def quicksort(x):
    if len (x) <= 1:
        return x
    menor, igual, maior = [], [], []
    p = x[0]
    for i in x:
        if i < p:
            menor.append(i)
        elif i == p:
            igual.append(i)
        else:
            maior.append(i)
    return quicksort(menor) + igual + quicksort(maior)

entrada = input().split()
N = int(entrada[0])
T = int(entrada[1])
times=[[]*T]
dicJogadores = {}
listaHabilidades = [None]*N
for i in range(N):
    j = input().split()
    dicJogadores[int(j[1])] = j[0]
    listaHabilidades[i] = int(j[1])

saida = quicksort(listaHabilidades)

while len(saida)>0:
    for t in range(len(times)):
        jogador = saida.pop(-1)
        times[t].append("%s %i"%(dicJogadores[jogador],jogador))

#format output
for k in range(len(times)):
    print("Time %i" %(k+1))
    for j in range(len(times[k])):
        print("%s" %times[k][j])
    print("")