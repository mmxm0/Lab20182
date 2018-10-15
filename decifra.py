'''
No PIOR CASO assumindo que a entrada seja de 104 caracteres, serão feitas 2704 iterações

'''

alfabetoCriptografado = input()
alfabeto = "abcdefghijklmnopqrstuvwxyz"
segredo = input()
saida = ""
cont = 0
for j in range(len(segredo)):
    for i in range(26):
        if segredo[j] == alfabetoCriptografado[i]:
            saida+=alfabeto[i]
        cont += 1

print(saida)