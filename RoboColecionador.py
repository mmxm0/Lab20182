# lógica dos Ventos
#D: -1
#E: +1

def giro(direcao, x=0):
    dic = {"L": 0, "N": 1, "O": 2, "S": 3}
    n = dic[direcao]
    n += x
    if n > 3:
        n = 0
    if n < 0:
        n = 3
    '''   d = { 0:"Sua direção atual é o LESTE", 1:"Sua direção atual é o NORTE",
            2:"Sua direção atual é o OESTE", 3: "Sua direção atual é o SUL"}

    print(d[n])'''
    return n


def caminha(direcao,posicao):
    if direcao == "L":
        posicao[0]+=1
    elif direcao == "N":
        posicao[1]+=1
    elif direcao =="O":
        posicao[0]-=1
    elif direcao == "S":
        posicao[1]-=1
    return posicao

def validPosicao(matriz,pos):
    try:
        n = matriz[pos]
        return True
    except KeyError:
        return False

sequencia = "DEDDEEEEDE"
m = 2
dicNum = {0:"L", 1:"N", 2:"O", 3:"S"}
dic = {"L": 0, "N": 1, "O": 2, "S": 3}
posicaoAtual = [1,1]
arena ={}
figurinhas = []
saida = 0
for i in sequencia:
    k = dicNum[m]
    if i=="D":
        m = giro(k,-1)
    elif i=="E":
        m = giro(k,1)
    elif i=="F":
        pass
