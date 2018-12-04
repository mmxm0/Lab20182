class NoAvl():
    def __init__(self, Chave, dado):
        self._dado = dado
        self._Chave = Chave
        self._esquerda = None
        self._direita = None
        self._pai = None
        self._altura = -1

    def setPai(self, pai):
        self._pai = pai

    def getPai(self):
        return self._pai

    def setChave(self, Chave):
        self._Chave = Chave

    def getChave(self):
        return self._Chave

    def setDireito(self, direita):
        self._direita = direita

    def getDireito(self):
        return self._direita

    def getDado(self):
        return self._dado

    def setDado(self, dado):
        self._dado = dado

    def setEsquerdo(self, esquerda):
        self._esquerda = esquerda

    def getEsquerdo(self):
        return self._esquerda

    def getAltura(self):
        return self._altura

    def setAltura(self, altura):
        self._altura = altura

    def ehEsquerdo(self):
        if self._pai.getChave() == None:
            return None
        else:
            if self._pai.getEsquerdo() == self:
                return True
            else:
                return False

    def ehDireito(self):
        if self._pai.getChave() == None:
            return None
        else:
            if self._pai.getDireito() == self:
                return True
            else:
                return False

    def noIrmao(self):
        if self._pai == None:
            return None
        else:
            if self.ehEsquerdo():
                return self._pai.getDireito()
            else:
                return self._pai.getEsquerdo()


class ArvoreAvl():
    def __init__(self):
        self._raiz = None
        self.printar = []
        self.PercPrintar = []

    def getRaiz(self):
        return self._raiz

    def getPercPrintar(self):
        return self.PercPrintar

    def getPrintar(self):
        return self.printar

    def pesquisar(self, Chave):
        no = self._raiz
        nivel = 1
        while no is not None and Chave != no.getChave():
            if Chave < no.getChave():
                nivel += 1
                no = no.getEsquerdo()
            else:
                nivel += 1
                no = no.getDireito()
        if no is not None:
            return str(nivel)
        else:
            return "-1"

    def altura(self, no):
        if no is None:
            return -1
        hEsquerda = self.altura(no.getEsquerdo())
        hDireita = self.altura(no.getDireito())
        no.setAltura(1 + self.maximo(hEsquerda, hDireita))
        return (1 + self.maximo(hEsquerda, hDireita))

    def fatorBalanceamento(self, no):
        fator = self.altura(no.getDireito()) - self.altura(no.getEsquerdo())
        return fator

    def maximo(self, x, y):
        if x > y:
            return x
        return y

    def rotEsquerda(self, no):
        pivo = no.getDireito()
        no.setDireito(pivo.getEsquerdo())
        if no.getDireito() is not None:
            no.getDireito().setPai(no)
        pivo.setEsquerdo(no)
        pivo.setPai(no.getPai())
        if no.getPai() is None:
            self._raiz = pivo
        else:
            if no.ehEsquerdo():
                no.getPai().setEsquerdo(pivo)
            else:
                no.getPai().setDireito(pivo)
        no.setPai(pivo)

    def rotDireita(self, no):
        pivo = no.getEsquerdo()
        no.setEsquerdo(pivo.getDireito())
        if no.getEsquerdo() is not None:
            no.getEsquerdo().setPai(no)
        pivo.setDireito(no)
        pivo.setPai(no.getPai())
        if no.getPai() is None:
            self._raiz = pivo
        else:
            if no.ehEsquerdo():
                no.getPai().setEsquerdo(pivo)
            else:
                no.getPai().setDireito(pivo)
        no.setPai(pivo)

    def adicionar(self, Chave, dado):
        no = NoAvl(Chave, dado)
        pivo = self._raiz
        pai = None
        while pivo is not None:
            pai = pivo
            if no.getChave() < pivo.getChave():
                pivo = pivo.getEsquerdo()
            else:
                pivo = pivo.getDireito()
        no.setPai(pai)
        paiNo = no.getPai()
        if pai is None:
            self._raiz = no
        else:
            if Chave < pai.getChave():
                pai.setEsquerdo(no)
            else:
                pai.setDireito(no)

        self.balancear(paiNo)

    def deletar(self, Chave):
        no = self.pesquisar(Chave)
        if no != None:
            print('Deletando ' + str(no.getChave()))
        if no == None:
            return ''
        paiNo = no.getPai()
        if no.getEsquerdo() == None or no.getDireito() == None:
            aux = no
        else:
            aux = self.sucessor(no)
        if aux.getEsquerdo() != None:
            aux2 = aux.getEsquerdo()
        else:
            aux2 = aux.getDireito()
        if aux2 != None:
            aux2.setPai(aux.getPai())
        if aux.getPai() == None:
            self._raiz = aux2
        else:
            if aux == aux.getPai().getEsquerdo():
                aux.getPai().setEsquerdo(aux2)
            else:
                aux.getPai().setDireito(aux2)
        if aux != aux2:
            no.setChave(aux.getChave())
        if paiNo == None:
            self.balancear(self._raiz)
        else:
            self.balancear(paiNo)
        return aux

    def balancear(self, no):

        while no is not None:
            altura = self.fatorBalanceamento(no)
            if altura > 1:
                if self.fatorBalanceamento(no.getDireito()) == -1:
                    self.rotDireita(no.getDireito())
                self.rotEsquerda(no)
            elif altura < -1:
                if self.fatorBalanceamento(no.getEsquerdo()) == 1:
                    self.rotEsquerda(no.getEsquerdo())
                self.rotDireita(no)
            no = no.getPai()

    def percorrer(self, no):
        if no != None:
            self.percorrer(no.getEsquerdo())
            self.PercPrintar.append(str(no.getChave()))
            self.percorrer(no.getDireito())
        else:
            pass

    def posOrdem(self, no, menor, maior):
        if no != None:
            self.percorrer(no.getEsquerdo())
            self.percorrer(no.getDireito())
            self.PercPrintar.append(str(no.getChave()))
        else:
            pass

    def ordem(self, menor, maior):
        lista = self.getPercPrintar()
        auxOrdem = []
        auxOrdem1 = ''
        for i in lista:
            i = int(i)
            if i >= menor and i <= maior:
                auxOrdem.append(i)
        for i in range(len(auxOrdem)):
            auxMin = min(auxOrdem)
            ind = auxOrdem.index(auxMin)
            r = auxOrdem.pop(ind)
            if auxMin not in auxOrdem:
                auxOrdem1 += str(auxMin)
                auxOrdem1 += " "
        return auxOrdem1


saida = ''
C = int(input())  # quantidade de gêneros que serão catalogados 1 à 10^5 -1
for genero in range(C):
    arvoreGenero = ArvoreAvl()
    comando = input()
    comando = comando.split()
    while comando[0] != "F":
        if comando[0] == "I":
            arvoreGenero.adicionar(int(comando[1]), "null")
        elif comando[0] == "N":
            saida += str(arvoreGenero.pesquisar(int(comando[1]))) + "\n"
        elif comando[0] == "L":
            pivo1 = int(comando[1])
            pivo2 = int(comando[2])
            arvoreGenero.posOrdem(arvoreGenero.getRaiz(), pivo1, pivo2)
            saida += str(arvoreGenero.ordem(pivo1, pivo2)) + "\n"
        comando = input()
        comando = comando.split()
    saida += "\n"
print(saida[:-2:])