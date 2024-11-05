# Proszę napisać program, który umożliwia zamianę
# dowolnej liczby naturalnej z jednego 
# systemu liczb w drugi w zależności od wyboru 
# użytkownika (na wejściu). Należy rozważyć 
# następujące systemy liczbowe: dwójkowy, ósemkowy, dziesiętny, szesnastkowy.

liczba = input("podaj liczbę: ")
systemy = [2,8,10,16]

system = int(input("podaj w jakim systemie jest podana liczba | do wyboru 2/8/10/16: "))
docelowy = int(input("podaj docelowy system liczbowy | do wyboru 2/8/10/16: "))
while system not in systemy or docelowy not in systemy:
    system = int(input("podaj w jakim systemie jest podana liczba jeszcze raz | do wyboru 2/8/10/16: "))
    docelowy = int(input("podaj docelowy system liczbowy jeszcze raz | do wyboru 2/8/10/16: "))
def zamiana_na_10(x,y):
    return(int(x,y))
    


def zamiana_z_10(liczba ,system):
    wynik = ""
    if system == 16:
        while liczba > 0:
            reszta = liczba % system
            if reszta == 10:
                reszta = "A"
            elif reszta == 11:
                reszta = "B"
            elif reszta == 12:
                reszta = "C"
            elif reszta == 13:
                reszta = "D"
            elif reszta == 14:
                reszta = "E"
            elif reszta == 15:
                reszta = "F"
            liczba = liczba // system
            wynik += str(reszta) 
    else:
        while liczba > 0:
            reszta = liczba % system
            liczba = liczba // system
            wynik += str(reszta)
    return wynik[::-1]

if system == 10:
    print(zamiana_z_10(int(liczba),docelowy))
else:
    liczba = zamiana_na_10(liczba,system)
    print(zamiana_z_10(liczba,docelowy))