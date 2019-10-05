"""
quebrando a banca por Brunna Arruda
"""
def acharMaior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if maior < lista[i]:
            maior = lista[i]
    return maior
def acharIndice(objeto,lista):
    for i in range(len(lista)):
        if lista[i] == objeto:
            return i
def listar(string):
    lista = [None for x in range(len(string))]
    for i in range(len(lista)):
        lista[i]=int(string[i])
    return lista

while True:
    saida = ''
    entrada = input().split(' ')
    caracteres = int(int(entrada[0])-int(entrada[1]))
    digitos = listar(input())
    posicaoInicial = 0
    for i in range(caracteres):
        for i in range(posicaoInicial-1):
            digitos[i] = 0
        maior = acharMaior(digitos[posicaoInicial:len(digitos)-caracteres+i+1])
        posicaoInicial = acharIndice(maior,digitos)+1
        saida+=str(maior)
    print(saida)
