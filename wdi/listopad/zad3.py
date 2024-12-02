aryt = [9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96]
geo = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480, 40960, 81920, 163840, 327680, 655360, 1310720, 2621440, 5242880]
chat = [81, 14, 98, 17, 71, 16, 68, 22, 5, 92, 14, 74, 45, 48, 42, 99, 30, 84, 24, 50, 
49, 16, 35, 83, 73, 51, 79, 3, 54, 58, 63, 87, 72, 29, 9, 60, 8, 13, 91, 55, 
64, 69, 23, 89, 24, 19, 97, 37, 8, 70, 36, 14, 10, 27, 34, 12, 33, 18, 28, 75, 
95, 31, 20, 62, 46, 53, 16, 38, 8, 43, 4, 39, 100, 52, 26, 28, 66, 93, 15, 32, 
16, 90, 7, 65, 40, 8, 1, 47, 44, 76, 59, 21, 61, 67, 78, 12, 80, 2, 86, 11]

import random
array = [random.randint(1,20) for j in range(100000)]

def ciagi(tablica):
    roznice = []
    ile_a = 0
    ile_g = 0 
    iloczyny = []
    for x in range(len(tablica)-1): 
        
        roznica = tablica[x] - tablica[x+1]
        roznice.append(roznica)
        iloczyn = tablica[x] / tablica[x+1]
        iloczyny.append(iloczyn)
        
    dlugosc = 1
    for i in range(1, len(roznice)):
        if roznice[i] == roznice[i-1]:
            dlugosc += 1 
        else:
            dlugosc = 1 
        if dlugosc == 3:
            ile_a +=1 
            
    dlugosc = 1
    for i in range(1, len(iloczyny)):
        if iloczyny[i] == iloczyny[i-1]:
            dlugosc += 1 
        else:
            dlugosc = 1 
        if dlugosc == 3:
            ile_g +=1 
    print(ile_a, ile_g)
    
    if ile_a > ile_g:
        return 1 
    elif ile_a == ile_g:
        return 0
    else: 
        return -1
            
ciagi(array)