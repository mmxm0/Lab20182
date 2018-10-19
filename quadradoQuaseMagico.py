def somaCol(matriz):
    soma=0
    colunas=[]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            soma+=matriz[j][i]
        colunas.append(soma)
        soma=0
    return colunas
def descobre(l):
    dif = 0 #index do numero que eu quero
    for i in range(len(l)-1):
        if l.count(l[i])<l.count(l[i+1]):
            dif = i
            break
    return dif

n = int(input())
cont = 0
quadrado = [[]]*n
somaLinhas = []

dic = {}
while cont<n:
    
    linha = input().split()
    linha = [int(x) for x in linha]
    somaLinhas.append(sum(linha))
    quadrado[cont]=linha
    cont+=1

somaColunas = somaCol(quadrado)

print(quadrado, somaLinhas, descobre(somaLinhas))
