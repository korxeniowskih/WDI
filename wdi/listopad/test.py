import random

N = int(input('Podaj dlugosc listy: '))
M = int(input('Podaj granice gorna zakresu: '))
L = int(input('Podaj granice golna zakresu: '))

if M > L:
    M, L = L, M

lista = [random.randint(M, L) for i in range(N)]

print(lista)

dlugosc = 1
dlugosc_max= 1
i_start_max = 0
i_start = 0

for i in range(0, len(lista)-1):
    if lista[i] <= lista[i+1]:
        if dlugosc == 1:
            i_start = i
        dlugosc += 1
    else:
        if dlugosc > dlugosc_max:
            dlugosc_max = dlugosc
            i_start_max = i_start
        dlugosc = 1
else:
    if dlugosc > dlugosc_max:
        dlugosc_max = dlugosc
        i_start_max = i_start
print(i_start_max)
print(dlugosc_max)


najdluzszy_podciag = lista[i_start_max:i_start_max+dlugosc_max]
suma = sum(najdluzszy_podciag)

print('Najdłuższy podciąg rosnący: ', najdluzszy_podciag)
print('Suma najdłuższego podciągu rosnącego: ', suma)