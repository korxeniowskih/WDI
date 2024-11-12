import random   
wymiar = int(input("podaj wymiar tablicy: "))
tablica = []
przykladowa_tablica_tak = [[27, 852, 485, 714], [323, 644, 940, 203], [777, 64, 249, 972], [572, 282, 510, 999]]
przykladowa_tablica_nie = [[24, 852, 485, 714], [313, 644, 940, 203], [701, 64, 249, 972], [418, 282, 510, 999]]

for x in range(wymiar):
    wiersz = []
    for i in range(wymiar):
        wiersz.append(random.randint(0,1000))
    tablica.append(wiersz)

def Zbudowana_z_pierwszych(x):
    pierwsze = [2,3,5,7]
    while x > 0:
        if x % 10 not in pierwsze:
            return False
        x = x // 10
    else:
        return True

def Czy_w_wierszu(tablica):
    for wiersze in tablica:
        for liczba in wiersze:
            if Zbudowana_z_pierwszych(liczba):
                break
        else:
            return "nie każdy wiersz zawiera \n"
    else:
        return "każdy wiersz zawiera \n"

for x in tablica:
    print(x)
print(Czy_w_wierszu(tablica))

for i in przykladowa_tablica_nie:
    print(i)
print(Czy_w_wierszu(przykladowa_tablica_nie))
    
for j in przykladowa_tablica_tak:
    print(j)  
print(Czy_w_wierszu(przykladowa_tablica_tak))