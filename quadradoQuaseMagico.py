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
    espelho = []
    for i in l:
        espelho.append(l.count(i))
    return l.index(l[espelho.index(min(espelho))]),l.index(l[espelho.index(max(espelho))])

n = int(input())
cont = 0
quadrado = [[]]*n
somaLinhas = []

while cont<n:
    
    linha = input().split()
    linha = [int(x) for x in linha]
    somaLinhas.append(sum(linha))
    quadrado[cont]=linha
    cont+=1

somaColunas = somaCol(quadrado)

c = descobre(somaColunas)
l = descobre(somaLinhas)

s = somaColunas[1]
e = quadrado[l[0]][c[0]]
x= s - (sum(quadrado[l[0]])-e)

print("%i %i"%(x,e))
