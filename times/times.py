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
times=[[]]*T
dicJogadores = {}
listaHabilidades = [None]*N
for i in range(N):
    j = input().split()
    dicJogadores[int(j[1])] = j[0]
    listaHabilidades[i] = int(j[1])

saida = quickSort(listaHabilidades)
t = 0
#regra
while len(saida)>0:
    jogador = saida.pop(-1)
    s = "%s %i"%(dicJogadores[jogador],jogador)
    times[t].append(s)
    print(times[t], t)
    del dicJogadores[jogador]
    t+=1

#format output
for k in range(len(times)):
    print("Time %i" %(k+1))
    for j in range(len(times[k])):
        print("%s" %times[k][j])
    print("")
