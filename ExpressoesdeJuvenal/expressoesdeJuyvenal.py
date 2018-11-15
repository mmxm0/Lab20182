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
            saida = "ERRO, LISTA VAZIA"

        elif self._inicio == self._fim:
            saida = self._fim.getDado()
            self._inicio = None
            self._fim = None

        else:
            e = self._fim
            saida = e.getDado()
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

    def pop(self):
        return self.remover()


linha1 = int(input())
contador = 0


def casa(abre, fecha):
    d = {"[": "]", "{": "}", "(": ")"}
    try:
        compara = d[abre]
        if compara == fecha:
            b = True
        else:
            b = False
        return b
    except:
        return False

saidaFinal = ""
while contador < linha1:
    i = 0
    p = Pilha()
    cadeia = input()
    saida = "S"
    while i < len(cadeia):
        n = cadeia[i]
        try:
            while n in "({[":
                p.push(n)
                i += 1
                n = cadeia[i]

            s = p.pop()
            if casa(s, n):
                i += 1
            else:
                saida = "N"

        except IndexError:
            saida = "N"

    saidaFinal+=saida + "\n"
    contador+=1

print(saidaFinal[:-1])

