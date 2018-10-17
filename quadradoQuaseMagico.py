n = int(input())
cont = 0
quadrado = [[]]*n
while cont<n:
    linha = input().split()
    linha = [int(x) for x in linha]
    quadrado[cont]=linha
    cont+=1
print(quadrado)
