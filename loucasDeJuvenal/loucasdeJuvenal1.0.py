class No:
    def __init__(self, dados=None):
        self.__dado = dados
        self.__anterior = None
        self.__proximo = None

    def getProximo(self):
        return self.__proximo

    def setProximo(self, no):
        self.__proximo = no

    def getAnterior(self):
        return self.__anterior

    def setAnterior(self, no):
        self.__anterior = no

    def getDado(self):
        return self.__dado


class ListaEncadeada():

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._len = None

    def getInicio(self):
        return self._inicio

    def getFim(self):
        return self._fim

    def isVazia(self):
        if self._inicio is None:
            return True
        else:
            return False

    def inserir(self, dado):
        newno = No(dado)
        if self.isVazia():
            self._inicio = newno
            self._fim = newno
        else:
            self._fim.setProximo(newno)
            newno.setAnterior(self._fim)
            self._fim = newno

    def inserirFim(self, dado):
        newno = No(dado)
        if self.isVazia():
            self._inicio = newno
            self._fim = newno
        else:
            self._fim.setProximo(newno)
            newno.setAnterior(self._fim)
            self._fim = newno

    def pesquisar(self, dado):
        if self.isVazia():
            print("Erro, Lista Vazia")
        else:
            nov = No(dado)
            i = self._inicio
            while nov.getDado() != i.getDado():
                i = i.getProximo()
                if i is None:
                    break
            else:
                return i

    def remover(self):
        if self.isVazia():
            saida = "Lista Vazia"

        elif self._inicio == self._fim:
            saida = self._fim
            self._inicio = None
            self._fim = None

        else:
            e = self._inicio
            saida = e
            novoFim = e.getProximo()
            self._inicio = novoFim
            novoFim.setAnterior(None)
        return saida

    def removerDown(self):
        if self.isVazia():
            saida = "Lista Vazia"

        elif self._inicio == self._fim:
            saida = self._fim
            self._inicio = None
            self._fim = None

        else:
            e = self._fim
            saida = e
            novoFim = e.getAnterior()
            self._fim = novoFim
            novoFim.setProximo(None)
        return saida

    def listarPilha(self):
        saida = "["
        if self.isVazia():
            saida += " ]"
        else:
            k = self._fim

            while k is not None:
                saida += (str(k.getDado()) + ", ")
                k = k.getAnterior()
        s = saida[:-2:]
        s += "]"
        print(s)

    def listar(self):
        saida = []
        if self.isVazia():
            saida = None
        else:
            k = self._inicio

            while k is not None:
                saida.append(str(k.getDado()))
                k = k.getProximo()
        return saida

    def getLen(self):
        if self.isVazia():
            return 0
        else:
            k = self._inicio
            tamanho = 0
            while k is not None:
                tamanho += 1
                k = k.getProximo()
            return tamanho


class Pilha(ListaEncadeada):
    def push(self, dado):
        self.inserir(dado)

    def Pop(self):
        return self.remover()

    def pushDown(self, dado):
        self.inserirFim(dado)

    def popDown(self):
        return self.removerDown()

    def __repr__(self):
        return str(self.listar())


class Jogador:
    A = 0
    def __init__(self,lista):
        self._id = Jogador.A
        self._deck = lista
        Jogador.A +=1

    def getId(self):
        return self._id

    def getDeck(self):
        return self._deck

    def novoDeck(self):
        #self._deck = self._deck[::-1]
        deck = Pilha()
        for i in self._deck:
            deck.push(i)
        self._deck = deck
        return self._deck

    def devolveCarta(self):
        inicio = self._deck.getInicio().getDado()
        self._deck.Pop()
        self._deck.pushDown(inicio)


    def devolveCartaVez(self,cartaVez):
        self._deck.pushDown(cartaVez)

    def pegaCarta(self):
        return self._deck.Pop()

    def pegaCartaVez(self):
        return self._deck.Pop()#popDown()

    def getDadoTopo(self):
        return self._deck.getInicio().getDado()

    def semCartas(self):
        return self._deck.isVazia()

    def __repr__(self):
        return str(self._deck)


class Jogo:
    def __init__(self,jogadores, mesa):
        self._jogadores = jogadores
        self._mesa = mesa
        self._numRodadas = 0
        self._vencedor = []

    def getJogadores(self):
        return self._jogadores

    def getMesa(self):
        return self._mesa

    def numRodadas(self):
        return self._numRodadas

    def vencedor(self):
        return self._vencedor[0].getId()

    def rodada(self):
        cartaDaVez = self._mesa.pegaCartaVez().getDado()
        cont = 0
        while cont < len(self._jogadores):
            if self._jogadores[cont].getDeck().isVazia():
                ganhador = self._jogadores.pop(cont)
                self._vencedor.append(ganhador)

            elif self._jogadores[cont].getDadoTopo() == cartaDaVez:
                self._jogadores[cont].pegaCarta()
            else:
                self._jogadores[cont].devolveCarta()
            cont += 1
        self._mesa.devolveCartaVez(cartaDaVez)
        self._numRodadas += 1

    def jogoCompleto(self):
        for h in range(0,10000):
            self.rodada()
            if len(self._vencedor)==1:
                return self.vencedor()

        return "0"


entrada = int(input())
saida = ""
for festa in range(entrada):
    deckMesa = input().split()
    mesa = Jogador(deckMesa)
    mesa.novoDeck()
    jogadores = []
    
    while True:
        try:
            C = input()
            if C != "-1":
                C = C.split()
                convidado = Jogador(C)
                convidado.novoDeck()
                jogadores.append(convidado)

            else:
                break
        except EOFError:
            break
    jogo = Jogo(jogadores,mesa)
    saida+=str(jogo.jogoCompleto())+"\n"

print(saida[:-1])