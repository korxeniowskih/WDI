from random import randint
# N = int(input("podaj N: "))
# M = int(input("podaj M: "))
# L = int(input("podaj L: "))

N,M,L = 100, 1, 100

if L > M:
    M,L = L,M # jesli L jest wieksze to sie zamieniaja wartosciami 
    
lista = []
for x in range(0,N): #
    lista.append(randint(L,M)) # generowanie listy o dlugosci N 
    
index_start = 0
index_start_max = 0 
dlugosc = 1
dlugosc_max = 0 
for i in range(0,len(lista)-1):
    if lista[i] < lista[i+1]: 
        if dlugosc == 1:
            index_start = i
        dlugosc += 1
    else:
        if dlugosc > dlugosc_max:
            dlugosc_max = dlugosc
            index_start_max = index_start
        dlugosc = 1   
         
print("poczatkowy index to", index_start_max, "a długość to", dlugosc_max)        

podciag = lista[index_start_max:index_start_max+dlugosc_max]
suma_podciagu = sum(podciag)

print(lista)
print(podciag, suma_podciagu)