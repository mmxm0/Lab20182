def checkPosicao(posicao, mapa):
    try:
        p = mapa.index(posicao)
        return True
    except ValueError:
        return False

def mapeiaNavio(linha, coluna, listaNavio, parteNavio):
    pos = [linha, coluna]
    if checkPosicao(pos, parteNavio):
        listaNavio.append(pos)
        parteNavio.remove(pos)
        lista = mapeiaNavio(linha - 1, coluna, listaNavio, parteNavio)
        listaNavio.append(pos)
        lista.remove(pos)
        lista = mapeiaNavio(linha + 1, coluna, listaNavio, parteNavio)
        listaNavio.append(pos)
        lista.remove(pos)
        lista = mapeiaNavio(linha, coluna - 1, listaNavio, parteNavio)
        listaNavio.append(pos)
        lista.remove(pos)
        lista = mapeiaNavio(linha, coluna + 1, listaNavio, parteNavio)
        listaNavio.append(pos)
        lista.remove(pos)
    return listaNavio
    


entrada = input().split()
nlinhas, nColunas = int(entrada[0]), int(entrada[1])
matriz = []

for x in range(nlinhas):
    linha = input()
    lm = []
    for i in range(len(linha)):
        lm.append(linha[i])
    matriz.append(lm)
    
    
parteNavio = []

for x in range(nlinhas):
    for y in range(nColunas):
        pos = matriz[x][y]
        fragmentoNavio = []
        if pos == "#":
            fragmentoNavio.append(x)
            fragmentoNavio.append(y)
            parteNavio.append(fragmentoNavio)
            
navios = []
while len(parteNavio) != 0:
    posicao = parteNavio[0]
    listaNavio = []
    navios.append(mapeiaNavio(posicao[0], posicao[1], listaNavio, parteNavio))

qtddDisparos = input()
qtddDisparos = int(qtddDisparos)
disparos = []
todosDisparos = []
while qtddDisparos > 0:
    tiro = input().split()
    for t in tiro:
        t = int(t)
        t = t-1
        disparos.append(t)
    todosDisparos.append(disparos)
    disparos = []
    qtddDisparos -= 1

afundados = []

for navio in navios:
    navioMirror = []
    for parte in navio:
        for tiro in todosDisparos:
            if parte == tiro:
                navioMirror.append(parte)
    afundados.append(navioMirror)                
                
qtddNavios = len(navios)
qtddNaviosDestruidos = 0
for navio in range(0,qtddNavios):
    if len(navios[navio]) == len(afundados[navio]):
        qtddNaviosDestruidos += 1
print(qtddNaviosDestruidos)
