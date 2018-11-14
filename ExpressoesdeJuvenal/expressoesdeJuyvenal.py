def empilha(lista):
    pilha = []

    for i in range(len(lista)):
        if lista[i] == '{' or lista[i]=="[" or lista[i]=="{":
            pilha.append(lista[i])
        else:
            continue

    return pilha

def desempilha(lista, p):

    while len(p)>0:
        p = p.pop(0)
        if p == "{":
            pivo = "}"
        elif p == "[":
            pivo = "]"
        elif p == "(":
            pivo = ")"

        if pivo in lista:
            pivo2 = lista.index(pivo)
            lista.pop(pivo2)

    return lista

def splitter(n):
    l = [None]*len(n)
    for i in range(len(n)):
        l[i] = n[i]
    return l


saida = []
t = int(input())
c = []
for i in range(t):
    cadeia = input()
    cadeia = splitter(cadeia)
    c.append(cadeia)

for q in c:
    stack = empilha(q)
    saidaLista = desempilha(q,stack)
    if len(saidaLista)==0:

        saida.append("S")
    else:
        saida.append("N")

for s in saida:
    print(s)

