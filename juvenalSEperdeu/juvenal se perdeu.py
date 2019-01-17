class No:
    def __init__(self, dado, chave):
        self._dado = dado
        self._chave = chave
        self._esq = None
        self._dir = None
        self._pai = None

    def getDado(self):
        return self._dado

    def setDado(self, dado):
        self._dado = dado

    def getChave(self):
        return self._chave

    def setChave(self, chave):
        self._chave = chave

    def getEsq(self):
        return self._esq

    def setEsq(self, esq):
        self._esq = esq

    def getDir(self):
        return self._dir

    def setDir(self, Dir):
        self._dir = Dir

    def getPai(self):
        return self._pai

    def setPai(self, pai):
        self._pai = pai


    def __repr__(self):
        return self._chave


class Arvore:
    def __init__(self):
        self._raiz = None

    def getRaiz(self):
        return self._raiz

    def setRaiz(self, raiz):
        self._raiz = raiz

    def minimo(self, no):
        if no == None:
            return None
        else:
            while no.getEsq() != None:
                no = no.getEsq()
        return no

    def maximo(self, no):
        if no == None:
            return None
        else:
            while no.getDir() != None:
                no = no.getDir()
        return no

    def sucessor(self, no):
        if no.getDir() != None:
            no = no.getDir()
            return self.minimo(no)
        else:
            pai = no.getPai()
            while pai != None and no == pai.getDir():
                no = pai
                pai = pai.getPai()
            return pai

    def antecessor(self, no):
        if no.getEsq() != None:
            no = no.getEsq()
            return self.maximo(no)
        else:
            pass
        pai = no.getPai()
        while pai != None and no == pai.getEsq():
            no = pai
            pai = pai.getPai()
        return pai

    def pesquisar(self, chave):
        no = self._raiz
        while no != None and chave != no.getChave():
            if chave < no.getChave():
                no = no.getEsq()
            else:
                no = no.getDir()
        if no != None:
            return no

    def inserir(self, chave, dado):
        no = No(chave, dado)
        p = self._raiz
        pai = None
        while p != None:
            pai = p
            if no.getChave() < p.getChave():
                p = p.getEsq()
            else:
                p = p.getDir()
        no.setPai(pai)
        if pai == None:
            self._raiz = no
        else:
            if chave < pai.getChave():
                pai.setEsq(no)
            else:
                pai.setDir(no)
        return no

    def remover(self, chave):
        no = self.pesquisar(chave)
        if no.getEsq() == None or no.getDir() == None:
            aux = no
        else:
            aux = self.sucessor(no)
        if aux.getEsq() != None:
            aux2 = aux.getEsq()
        else:
            aux2 = aux.getDir()
        if aux2 != None:
            aux2.setPai(aux.getPai())
        if aux.getPai() == None:
            self._raiz = aux2
        else:
            if aux == aux.getPai().getEsq():
                aux.getPai().setEsq(aux2)
            else:
                aux.getPai().setDir(aux2)
        if aux != aux2:
            no.setChave(aux.getChave())

        return aux

    def posOrdem(self, no):
        string = ''
        if no != None:
            string += self.emOrdem(no.getEsq())
            string += self.emOrdem(no.getDir())
            string += (str(no.getChave()) + ' ')
            return string

    def preOrdem(self, no):
        string = ''
        if no != None:
            string += (str(no.getChave()) + ' ')
            string += self.emOrdem(no.getEsq())
            string += self.emOrdem(no.getDir())
        return string

    def emOrdem(self, no):
        string = ''
        if no != None and no.getChave() != None:
            string += self.emOrdem(no.getEsq())
            string += str(no.getChave() + ' ')
            string += self.emOrdem(no.getDir())
            return string
        return string

    def __repr__(self):
        string = self.emOrdem(self._raiz)
        return '[' + string[:-2] + ']'


def operacoes(arvore, entrada):
    saida = []
    for i in range(len(entrada)):
        if entrada[i].lower() == 'a':
            arvore.inserir(entrada[i + 1], entrada[i + 1])
        elif entrada[i].lower() == 'b':
            arvore.remover(entrada[i + 1])
        elif entrada[i].lower() == 'pre':
            if arvore.getRaiz() != None:
                saida.append(arvore.preOrdem(arvore.getRaiz()))
            else:
                saida.append('0 ')
        elif entrada[i].lower() == 'in':
            if arvore.getRaiz() != None:
                saida.append(arvore.emOrdem(arvore.getRaiz()))
            else:
                saida.append('0 ')
        elif entrada[i].lower() == 'post':
            if arvore.getRaiz() != None:
                saida.append(arvore.posOrdem(arvore.getRaiz()))
            else:
                saida.append('0 ')
        elif entrada[i].lower() == 'c':
            pesquisa = arvore.pesquisar(entrada[i + 1])
            if pesquisa == None:
                saida.append('0')
            elif arvore.antecessor(pesquisa) == None:
                saida.append('0')
            else:
                saida.append(arvore.antecessor(pesquisa))
    return saida


cont = 1
while True:
    try:
        qtd = int(input())
        entrada = ''
        for i in range(qtd):
            ent = input()
            entrada += ' ' + ent
        entrada = entrada.split(" ")
        arvore = Arvore()
        saida = operacoes(arvore,entrada)
        print("Caso %d:" % cont)
        for i in range(len(saida)):
            print(saida[i])
        cont += 1
    except:
        break