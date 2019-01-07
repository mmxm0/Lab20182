class No:
    def __init__(self, valor, listaArestas ={}, l=[]):
        self.__arestas = listaArestas
        self.__vertice = valor
        self.__distancia = float("inf")
        self.__antecessor = None
        self.listaLigacao = l

    def getArestas(self):
        return self.__arestas

    def getAresta(self, v):
        try:
            tupla = (self.__vertice, v)
            return self.__arestas[tupla]
        except KeyError:
            return None




    def setAresta(self, v, p):
        tupla = (self.__vertice, v)
        self.__arestas[tupla] = p

    def getVertice(self):
        return self.__vertice

    def getAntecessor(self):
        return self.__antecessor

    def setAntecessor(self, a):
        self.__antecessor = a

    def getDistancia(self):
        return self.__distancia

    def setDistancia(self, v):
        self.__distancia=v

class Grafo:

    def __init__(self, v=[]):
        self.__raiz = None
        self.__vertices = v

    def minimo(self):
        pivo = 0
        for i in range(1,len(self.__vertices)):
            if self.__vertices[i].getDistancia() < self.__vertices[pivo].getDistancia():
                pivo = i
        return self.__vertices[pivo]

    def setQ(self):
        conjuntoQ =[]
        for i in self.__vertices:
            conjuntoQ.append(i)
        return conjuntoQ


    def minimoQ(self, Q):
        pivo = 0
        for i in range(1,len(Q)):
            if Q[i].getDistancia() < Q[pivo].getDistancia():
                pivo = i
        if len(Q)>0:
            menor  = Q.pop(pivo)
            return menor


    def podeAtualizaQ(self, Q, i):
        b = False
        for j in Q:
            if j.getVertice() == i.getVertice():
                b =True
                break
        return b

    def getNode(self, v):
        for i in self.__vertices:
            if i.getVertice() == v:
                return i

    def djikstra(self,sai, chega):

        Q = self.setQ()

        self.__vertices[sai-1].setDistancia(0)
        self.__vertices[sai-1].setAntecessor(sai)
        while len(Q)>0:

            s = self.minimoQ(Q)
            u = self.__vertices[self.__vertices.index(s)]
            for i in u.listaLigacao:
                resultado = u.getAresta(i)
                v = resultado + u.getDistancia()
                node = self.getNode(i)
                if self.podeAtualizaQ(Q, node) and v < node.getDistancia():
                    node.setDistancia(v)
                    node.setAntecessor(i)
                    Q[Q.index(node)] = node

        return self.__vertices[chega-1].getDistancia()


a = No(1)
b = No(2)
c = No(3)
d = No(4)
e = No(5)
f = No(6)
a.listaLigacao = [2,4]
b.listaLigacao = [1,3]
c.listaLigacao = [2,4,5]
d.listaLigacao = [1,3,6]
e.listaLigacao = [3,6]
f.listaLigacao = [4,5]
a.setAresta(2,10)
a.setAresta(4, 20)
b.setAresta(1,10)
b.setAresta(3,2)
c.setAresta(2,2)
c.setAresta(4,1)
c.setAresta(5,1)
d.setAresta(1,20)
d.setAresta(3,1)
d.setAresta(6,6)
e.setAresta(3,1)
e.setAresta(6,3)
f.setAresta(4,6)
f.setAresta(5,3)
l= [a,b,c,d,e,f]
g = Grafo(l)

print(g.djikstra(1,6))