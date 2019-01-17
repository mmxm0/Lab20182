tLinhas = None
sColunas = None
t = 'ABAZDC'
s = 'BACBAD'
tabela = [[0]*len(s)]*len(t)

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] != t[j]:
            try:
                tabela[i][j] = max([tabela[i-1][j],tabela[i][j-1]])
            except ValueError:
                tabela[i][j] = 0
        if s[i] == t[j]:
            tabela [i][j] = 1+ tabela[i-1][j-1]
print(tabela)
print(tabela[len(s)-1][len(t)-1])