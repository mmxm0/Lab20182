

def giro(direcao, dirOuEsq=0):
    dic = {"L": 2, "N": 1, "O": 0, "S": 3}

    n = dic[direcao]
    n += dirOuEsq
    if n > 3:
        n = 0
    if n < 0:
        n = 3
    dic = {2: "L", 1: "N", 0: "O", 3: "S"}

    return dic[n]


def caminhaLeste(direcao,posicao, matriz):
    pivo = (posicao[0], posicao[1])
    if direcao == "L":
        posicao[1]-=1
    elif direcao == "N":
        posicao[0]-=1       #o decremento muda de acordo com a ordem inicial da posição
    elif direcao =="O":
        posicao[1]+=1
    elif direcao == "S":
        posicao[0]+=1
    if validPosicao(matriz, (posicao[0],posicao[1])):
        return (posicao[0],posicao[1])
    else:
        return pivo

def caminhaOeste(direcao,posicao, matriz):
    pivo = (posicao[0], posicao[1])
    if direcao == "L":
        posicao[1]+=1
    elif direcao == "N":
        posicao[0]+=1       #o decremento muda de acordo com a ordem inicial da posição
    elif direcao =="O":
        posicao[1]-=1
    elif direcao == "S":
        posicao[0]-=1
    if validPosicao(matriz, (posicao[0],posicao[1])):
        return (posicao[0],posicao[1])
    else:
        return pivo

def validPosicao(matriz,pos):
    try:
        n = matriz[pos]
        return True
    except KeyError:
        return False


def geraCaminho(ctte, posInicial, orientacao, matriz, sequencia):

    saida = {(posInicial[0],posInicial[1]):orientacao}

    for i in sequencia:
        if i == "D":
            orientacao= giro(orientacao,-1)
        elif i == "E":
            orientacao = giro(orientacao,+1)
        elif i =="F":
            if ctte in "LN":
                posInicial = caminhaLeste(orientacao, [posInicial[0],posInicial[1]],matriz)
            if ctte in "OS":
                posInicial = caminhaOeste(orientacao, [posInicial[0], posInicial[1]], matriz)
            saida[posInicial] = matriz[posInicial]

    return saida

def calculaFigurinhas(matriz):
    s = 0
    for i in matriz:
        if matriz[i] == "*":
            s+=1
    return s


saida = ""
while True:
    matriz = {}
    pLinha = input().split()
    pLinha = [int(c) for c in pLinha]
    if sum(pLinha) == 0:
        break
    orientacao = ""
    for linha in range(pLinha[0]):
        l = input()
        for coluna in range(pLinha[1]):
            t = (linha,coluna)
            if l[coluna] == "#":
                continue
            elif l[coluna] in "NOLS":
                posicaoAtual = [linha,coluna]
                orientacao = l[coluna]
                ctte = orientacao
                matriz[t] = l[coluna]
            else:
                matriz[t] = l[coluna]
    sequencia = input()
    resultado = geraCaminho(ctte,posicaoAtual,orientacao,matriz,sequencia)
    saida+=str(calculaFigurinhas(resultado))+"\n"
print(saida[:-1:])