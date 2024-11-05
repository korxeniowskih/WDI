import random   
wymiar = int(input("podaj wymiar tablicy: "))
tablica = []

for x in range(wymiar):
    wiersz = []
    for i in range(wymiar):
        wiersz.append(random.randint(0,1000))
    tablica.append(wiersz)

def Zbudowana_z_pierwszych(x):
    pierwsze = [2,3,5,7]
    x = str(x)
    for i in x:
        i = int(i)
        if i not in pierwsze:
            return False
    else:
        return True
    
print(tablica)

def Czy_w_wierszu(tablica):
    for wiersze in tablica:
        for liczba in wiersze:
            if Zbudowana_z_pierwszych(liczba):
                break
        else:
            return "nie każdy wiersz zawiera"
    else:
        return "każdy wiersz zawiera"
            
print(Czy_w_wierszu(tablica))
