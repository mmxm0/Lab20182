'''zcbedfghljkinmypqrutsvwxoa
cadeadonalisawelcometothejunglemelhormusicadogunsnroseseveradoroessamusicaachotopmaravilhosawelcometotejunglebaby'''
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabetoCriptografado = input()
entrada = input()
saida=''
cont=0
for j in range(len(entrada)):
    for i in range(26):
        if entrada[j] == alfabeto[i]:
            saida+=alfabetoCriptografado[i]
        cont += 1

print(saida,cont)