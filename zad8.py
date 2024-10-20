x = int(input("podaj wysokosc choinki: "))
for i in range(1,x+1):
    odstep= " " * (x-i)
    gwiazdki = "*" * (2*i-1)
    print(odstep,gwiazdki)
else:
    spacje_pien = ' ' * (x - 1)
    print(spacje_pien + "U")