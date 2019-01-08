class No:
    def __init__(self, valor, listaArestas ={}, l=[]):
        self.__arestas = listaArestas
        self.__vertice = valor
        self.__distancia = float("inf")
        self.__antecessor = None
        self.listaLigacao = l
        self.__distPar = float('inf')
        self.__distImpar = float('inf')
        self.__controle = None

    def getControle(self):
        return self.__controle

    def setControle(self, nc):

        self.__controle = nc

    def getArestas(self):
        return self.__arestas

    def getAresta(self, v):
        try:
            tupla = (self.__vertice, v)
            return self.__arestas[tupla]
        except KeyError:
            return None

    def getDistPar(self):
        return self.__distPar

    def getDistImpar(self):
        return self.__distImpar

    def setDistImpar(self, nd):
        self.__distImpar = nd

    def setDistPar(self, nd):
        self.__distPar = nd

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

    def minimoQpar(self, Qpar):
        pivo = 0
        for i in range(1,len(Qpar)):
            if Qpar[i].getDistPar() < Qpar[pivo].getDistPar():
                pivo = i
        if len(Qpar)>0:
            menor  = Qpar.pop(pivo)
            return menor

    def minimoQimp(self, Qimpar):
        pivo = 0
        for i in range(1,len(Qimpar)):
            if Qimpar[i].getDistImpar() < Qimpar[pivo].getDistImpar():
                pivo = i
        if len(Qimpar)>0:
            menor  = Qimpar.pop(pivo)
            return menor

    def minimoParImpar(self, Qpar, Qimpar):
        mPar = self.minimoQpar(Qpar)
        mImp = self.minimoQimp(Qimpar)
        if mPar < mImp:
            return mPar
        else:
            return mImp

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

    def djikstraModificado(self,sai, chega):

        self.__vertices[sai-1].setDistancia(0)
        self.__vertices[sai-1].setAntecessor(sai)
        self.__vertices[sai-1].setControle('par')
        Qpar = self.setQ()
        Qimpar = self.setQ()

        while len(Qpar)>0 and len(Qimpar)>0:

            s = self.minimoParImpar(Qpar, Qimpar)
            u = self.__vertices[self.__vertices.index(s)]

            for i in u.listaLigacao:
                resultado = u.getAresta(i)
                v = resultado + u.getDistancia()
                node = self.getNode(i)
                #TODO: Organizar o controle, como ele vai saber que é pra atualizar o par ou o impar?
                if self.podeAtualizaQ(Qpar, node) and v < node.getDistPar():
                    node.setDistPar(v)
                    node.setAntecessor(i)
                    Qpar[Qpar.index(node)] = node
                elif self.podeAtualizaQ(Qimpar, node) and v < node.getDistImpar():
                    node.setDistImpar(v)
                    node.setAntecessor(i)
                    Qimpar[Qimpar.index(node)] = node

        saida = self.__vertices[chega-1].getDistPar()

        if saida == float('inf'):
            return -1
        else: return saida


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