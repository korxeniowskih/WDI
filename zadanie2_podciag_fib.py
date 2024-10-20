while True:
    suma_podciagu = int(input("podaj liczbe: "))
    a,b = 0,1 
    x = 0 
    while x < suma_podciagu: 
        x+=b 
        a,b = b, b+a
    a,b = 0,1 

    while x != suma_podciagu:
        x-=b
        a,b = b, b+a
        if x < suma_podciagu or suma_podciagu<0:
            print("nie istnieje")
            break
    else:
        print("istnieje")
