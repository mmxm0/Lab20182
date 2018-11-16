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


class ListaDuplamenteEncadeada():
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

    def remover(self, dado):
        if self.isVazia():
            saida = "ERRO, LISTA VAZIA"

        elif self._inicio == self._fim:
            saida = self._fim.getDado()
            self._inicio = None
            self._fim = None

        else:
            pivo = self.pesquisar(dado)
            if pivo == None:
                return "Erro, elemento não está na lista"

            # ser o primeiro da lista
            elif pivo.getAnterior() == None:
                proximo = pivo.getProximo()
                saida = pivo.getDado()
                proximo.setAnterior(None)
                pivo.setProximo(None)
                self._inicio = proximo

            # ser o ultimo da lista

            elif pivo.getProximo() == None:
                anterior = pivo.getAnterior()
                anterior.setProximo(None)
                pivo.setAnterior(None)
                self._fim = anterior
                saida = pivo.getDado()

            else:
                proximo, anterior = pivo.getProximo(), pivo.getAnterior()
                proximo.setAnterior(anterior)
                anterior.setProximo(proximo)
                pivo.setAnterior(None)
                pivo.setProximo(None)
                saida = pivo.getDado()

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
        saida = ""
        if self.isVazia():
            saida = None
        else:
            k = self._inicio

            while k is not None:
                saida += str(k.getDado()) + " "
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


fila = ListaDuplamenteEncadeada()
N = int(input())
entrada = input()
M = int(input())
saida = input()
i = 0
idPessoa = ""
entrada+=" "
saida+=" "
for p in range(len(entrada)):
    if entrada[p] == " ":
        fila.inserir(idPessoa)
        idPessoa = ""
    else:
        idPessoa += entrada[p]
idPessoaSaida = ""
for o in range(len(saida)):
    if saida[o] == " ":
        fila.remover(idPessoaSaida)
        idPessoaSaida=""
    else: idPessoaSaida+=saida[o]

print(fila.listar())
