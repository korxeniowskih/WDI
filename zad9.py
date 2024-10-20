saldo = 1232422
pin = 1234

def wplata(x):
    global saldo
    saldo += x 
def wyplata(y):
    global saldo
    if y > saldo :
        return "brak wystarczajacych srodkow"
    else:
        saldo-=y
def stan_konta():
    global saldo
    return saldo
    
    
while True:
    operacja = int(input("Co chcesz zrobic w następnym kroku? 1 - wpłata | 2 - wypłata | 3 - sprawdzenie salda | 4 - koniec"))
    if operacja == 4:
        break
    w_p = int(input("podaj pin"))
    if w_p != pin: 
        continue
    if operacja == 1:
        kwota = int(input("podaj kwotę"))
        wplata(kwota)
    if operacja == 2:
        kwota = int(input("podaj kwotę"))
        wyplata(kwota)
    if operacja == 3:
        print(stan_konta())

    
    