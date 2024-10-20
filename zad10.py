from random import randint
def dodawanie(x,y):
    return x+y
def odejmowanie(x,y):
    return x-y
def mnozenie(x,y):
    return x*y
def dzielenie(x,y):
    return x/y
def potegowanie(x,y):
    return pow(x,y)
def losowanie(x,y):
    if y < x:
        x,y = y , x 
    if abs(x-y) > 1:
        return randint(x,y)
    else:
        return ":D"
def pierwiastkowanie(x,y):
    return pow(x,1/y)


while True: 
    a = int(input("podaj pierwszą liczbę"))
    b = int(input("podaj druga liczbę"))
    dzialanie = input("+ | - | / | * | # |  ^ | x")
    if dzialanie == "+":
        print(dodawanie(a,b))
    elif dzialanie == "-":
        print(odejmowanie(a,b))
    elif dzialanie == "/":
        print(dzielenie(a,b))
    elif dzialanie == "*":
        print(mnozenie(a,b))
    elif dzialanie == "#":
        print(pierwiastkowanie(a,b))
    elif dzialanie == "^":
        print(potegowanie(a,b))
    elif dzialanie == "x":
        print(losowanie(a,b))
    else:
        print("błędnie wprowadzony symbol działania")
        continue
    l = None    
    while l != "N" and l != "T":
        l = input("Czy chcesz wprowadzić nowe dane (T/N)")
    if l == "N":
        break        
    

    