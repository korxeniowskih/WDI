from time import sleep
def potega(M,N):
    if N == 0:
        return 1
    return M * potega(M,N-1)
        
def pierwsza(x, dzielnik):
    if dzielnik == 1:
        return True
    if x % dzielnik == 0:
        return False
    else:
        return pierwsza(x,dzielnik-1)

M = int(input("Podaj liczbę"))
N = int(input("Podaj wykładnik"))
if pierwsza(N,round(pow(N,1/2))):
    sleep(M)

print(potega(M,N))