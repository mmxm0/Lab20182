def dijkstra(grafo, vizinhos):
    resultado = []
    for x in range(len(grafo)):
        distancia = [float("inf")] * len(grafo)
        vertice = [0] * len(grafo)
        distancia[x] = 0
        while 0 in vertice:
            minimo = float("inf")
            for h in range(len(vertice)):
                if vertice[h] == 0 and distancia[h] < minimo:
                    minimo = distancia[h]
                    posi = h
            vertice[posi] = True
            for q in range(len(distancia)):
                if vertice[q] != 1:
                    if vizinhos[posi][q] == 1:
                        valor1 = distancia[posi] + grafo[posi][q]
                        if valor1 < distancia[q]:
                            distancia[q] = valor1

        maximo = calcMaximo(distancia)
        resultado.append(maximo)
    return (resultado)


def setGrafo(valor):
    matriz = []
    for i in range(valor):
        linha = (valor) * [0]
        matriz.append(linha)
    return matriz


def calcMaximo(listaa):
    y = 0
    for w in (listaa):
        if w > y:
            y = w
    return y


def calcMinimo(listaa):
    y = float("inf")
    for w in (listaa):
        if w < y:
            y = w
    return y


entrada = input().split()
cidades, voos = int(entrada[0]), int(entrada[1])
grafo = setGrafo(cidades)
vizinhos = setGrafo(cidades)
for j in range(voos):
    dado = input().split()
    c1, c2, p = int(dado[0]), int(dado[1]), int(dado[2])
    grafo[c1][c2] = int(p)
    grafo[c2][c1] = int(p)
    vizinhos[c1][c2] = 1
    vizinhos[c2][c1] = 1
maximos = dijkstra(grafo, vizinhos)
minoo = calcMinimo(maximos)
print(minoo)