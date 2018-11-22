n = int(input())
entrada = input().split()
entrada = [int(i) for i in entrada]
ordenados = [i for i in range(1,n+1)]
contador = 0

for o in ordenados:
    for elem in entrada:
        if elem > o:
            contador+=1
        elif elem < o:
            continue
        elif elem == o:
            break

print(contador)