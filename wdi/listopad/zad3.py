aryt = [9, 12, 15, 18, 21, 24, 27, 30, 33, 36 , 3, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96]
geo = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480, 40960, 81920, 163840, 327680, 655360, 1310720, 2621440, 5242880]

import random
array = [random.randint(1,20) for j in range(100000)]

def ciagi(ciag):
    roznice = [ciag[i] - ciag[i + 1] for i in range(len(ciag) - 1)]
    ilorazy = [ciag[i] / ciag[i + 1] for i in range(len(ciag) - 1)]
        
    def zlicz_ciagi(wartosci):
        dlugosc = 1
        licznik = 0
        for i in range(1, len(wartosci)):
            if wartosci[i] == wartosci[i - 1]:
                dlugosc += 1
            else:
                dlugosc = 1
            if dlugosc == 3:
                licznik += 1
        return licznik
    
    ile_a = zlicz_ciagi(roznice)
    ile_g = zlicz_ciagi(ilorazy)
    print(ile_a, ile_g)
    
    if ile_a > ile_g:
        return 1 
    elif ile_a == ile_g:
        return 0
    else: 
        return -1
            
ciagi(aryt) #
