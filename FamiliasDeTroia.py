#Conjuntos Disjuntos com Union-Find
class No:
    def __init__(self, listaArestas, v):
        self.arestas = listaArestas
        self.vertice = v

class Grafo:
    def __init__(self,arestas,vertices):
        self.arestas = arestas
        self.vertices = vertices
        self.inicio = None

    def union(self,Q, u, v):
        p1 = self.find(Q,u)
        p2 = self.find(Q,v)
        if len(p2) >1:
            for i in p2:
                Q[Q.index(p1)].append(i)
        else:Q[Q.index(p1)].append(v)
        Q.pop(Q.index(p2))
        return Q

    def find(self, Q,vertice):
        for i in Q:
            for j in i:
                if j == vertice:
                    return i


    def Conecta(self):
        Q = []
        for v in self.vertices:
            Q.append([v])
        for e in self.arestas:
            if self.find(Q,e[0]) != self.find(Q,e[1]):
                novoQ = self.union(Q,e[0],e[1])
                Q =  novoQ
        return len(Q)


#mock
#v = [i for i in range(1,6+1)]
#a = [(5,6),(4,2),(1,2),(3,4),(2,6)]

l1 = input().split()
n = int(l1[0])
v = [i for i in range(1,n+1)]
a = [] #lista de arestas
cont = 0
while cont < int(l1[1]):
    edg = input().split()
    e = (int(edg[0]),int(edg[1]))
    a.append(e)
    cont+=1

g = Grafo(a,v)
print(g.Conecta())
