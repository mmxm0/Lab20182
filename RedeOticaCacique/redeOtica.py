#import numpy as nx

class Aresta:
    def __init__(self, x=None, y=None, z=float('inf')):
        self.__start = x
        self.__end = y
        self.__peso = z
        self.__id = "%s %s" %(str(x),str(y))

    def getId(self):
        return self.__id

    def getStart(self):
        return self.__start

    def getEnd(self):
        return self.__end

    def getPeso(self):
        return self.__peso

    def setPeso(self, p):
        self.__peso = p

    def setEnd(self, e):
        self.__end = e

    def setStart(self, s):
        self.__start = s

    def __repr__(self):
        return "("+str(self.__start)+", "+str(self.__end)+", "+str(self.__peso)+")"


class Vertice:
    def __init__(self, nome=None):#, lequeIn=[], lequeOut=[]):
        self.__v = nome
        #self.__in = lequeIn
        #self.__out = lequeOut
        self.__cor = None
        self.__distancia = None
        self.__predecessor = None
        self.__d = None
        self.__f = None

    def setD(self,d):
        self.__d  =d

    def setF(self,f):
        self.__f = f

    def getD(self):
        return self.__d

    def getF(self):
        return self.__f

    def getV(self):
        return self.__v

    def setV(self,nv):
       self.__v = nv

    def getDistancia(self):
        return self.__distancia

    def setDistancia(self,d):
        self.__distancia = d

    def getCor(self):
        return self.__cor

    def setCor(self,c):
        self.__cor = c

    def getPredecessor(self):
        return self.__predecessor

    def setPredecessor(self,p):
        self.__predecessor = p



    def __repr__(self):
        return str(self.__v)


class BinHeap(Vertice):#Aresta):
    def __init__(self):
        super().__init__()
        self.heapLista = [0]
        self.tamAtual = 0

    def percUp(self, n):
        while i // 2 > 0:
            if self.heapLista[i] < self.heapLista[i // 2]:
                tmp = self.heapLista[i // 2]
                self.heapLista[i // 2] = self.heapLista[i]
                self.heapLista[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapLista.append(k)
        self.tamAtual += 1
        self.percUp(self.tamAtual)

    def percDown(self, i):
        while (i * 2) <= self.tamAtual:
            mc = self.minFilho(i)
            if self.heapLista[i].getPeso() > self.heapLista[mc].getPeso():
                    tmp = self.heapLista[i]
                    self.heapLista[i] = self.heapLista[mc]
                    self.heapLista[mc] = tmp
            i = mc

    def minFilho(self, i):
        if i * 2 + 1 > self.tamAtual:
            return i * 2
        else:
            if self.heapLista[i * 2].getPeso() < self.heapLista[i * 2 + 1].getPeso():
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapLista[1]
        self.heapLista[1] = self.heapLista[self.tamAtual]
        self.tamAtual = self.tamAtual - 1
        self.heapLista.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.tamAtual = len(alist)
        self.heapLista = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        return self.heapLista


class Grafo():

    def __init__(self, arestas, vertices):
        self.__arestas = [Aresta(*edge) for edge in arestas]
        self.__vertices = list(Vertice(e)for e in range(1,vertices+1))
        self.__list = self.adj()

    def getRaiz(self):
        return self.__vertices[0]

    def getVerticeX(self,x):
        return self.__vertices[x-1]

    def getArestaX(self,tuplaAresta):
        for a in self.__arestas:
            if a.getId() == tuplaAresta:
                volta = a
                break
        return a

    def adj(self):
        listaAdj ={}
        for i in self.__vertices:
            listaAdj[i] =[]
            for j in self.__arestas:
                if j.getStart() == i.getV(): #leque de saída
                    listaAdj[i].append(self.__vertices[j.getEnd()-1])
                if j.getEnd() == i.getV() and self.__vertices[j.getStart()-1] not in listaAdj[i]: #leque de entrada
                    listaAdj[i].append((self.__vertices[j.getStart()-1]))

        return listaAdj

    def kruskal(self):
        s = []
        conjunto = []
        for v in self.__vertices:
            c = self.makeSet(v, conjunto)
            conjunto.append(c)
        q = self.ordenaHeap()
        for e in q:
            u = self.getVerticeX(e.getStart())
            v = self.getVerticeX(e.getEnd())
            if self.findSet(u, conjunto) != self.findSet(v, conjunto):
                s.append((e.getStart(), e.getEnd()))
                conjunto = self.union(u, v, conjunto)

        return s

    def findSet(self, x, conjunto):
        #print(conjunto)
        pont = None
        for i in conjunto:
            if x in i:
                pont = conjunto.index(i)
        return pont

    def union(self, x, y, conjunto):
        novoConjunto = []
        ponteiroX = self.findSet(x, conjunto)
        ponteiroY = self.findSet(y, conjunto)
        Sx = conjunto[ponteiroX]
        Sy = conjunto[ponteiroY]
        for i in Sy:
            Sx.append(i)
        novoConjunto.append(Sx)
        for i in conjunto:
            if i != conjunto[ponteiroX] and i != conjunto[ponteiroY]:
                novoConjunto.append(i)
        return novoConjunto

    def ordenaHeap(self):
        q = self.__arestas.copy()
        heapMin = BinHeap()
        heapMin.buildHeap(q)
        qOrdenado = []
        for i in q:
            menor = heapMin.delMin()
            qOrdenado.append(menor)
        return qOrdenado



    def makeSet(self,x,conjunto): #conjunto pode estar vazio
        pode = True
        for i in conjunto:
            if x in i:
                pode = False
        if pode:
            sx = [x]
        return sx
saida = ""

def bubbleSort(nlist):
    for x in range(len(nlist)):
        if nlist[x][0] > nlist[x][1]:
            novatupla = (nlist[x][1],nlist[x][0])
            nlist[x] = novatupla

    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i][0]>nlist[i+1][0]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
            elif nlist[i][0]==nlist[i+1][0]:
                if nlist[i][1]>nlist[i+1][1]:
                    temp = nlist[i]
                    nlist[i] = nlist[i + 1]
                    nlist[i + 1] = temp


    return nlist

def formatOutput(outs,qtddteste):
    global saida
    saida+="Teste %i\n"%qtddteste
    for i in outs:
        saida+="%i %i\n"%(i[0],i[1])
    saida+="\n"


nm = input()#.split()
qtdd = 0
while nm != "0 0":
    try:
        nm = nm.split()
        n = int(nm[0])
        m = int(nm[1])
        arestas = []
        for i in range(m):
            rede = input().split()
            arestas.append((int(rede[0]),int(rede[1]),int(rede[2])))
        grafo = Grafo(arestas,n)
        qtdd+=1
        out = (grafo.kruskal())
        outs = bubbleSort(out)
        formatOutput(outs,qtdd)
        nm = input()
    except IndexError:
        break
print(saida[:-2:])