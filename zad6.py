liczba_1 = int(input("podaj pierwsza liczbę"))
liczba_2 = int(input("podaj druga liczbę"))

if liczba_2 and liczba_1 < 0:
    print("wprowadzone liczby sa mniejsze od 0")
else:
    liczba_1, liczba_2 = abs(liczba_1), abs(liczba_2) 
    suma = liczba_1 + liczba_2
    roznica = liczba_1 - liczba_2
    iloczyn = liczba_2 * liczba_1
    iloraz = liczba_1/liczba_2
    kwadrat1 = pow(liczba_1,2)
    kwadrat2 = pow(liczba_2,2)

    pierwiastek1 = pow(liczba_1,1/2)
    pierwiastek2 = pow(liczba_2,1/2)
    
    
    print(
        "suma, roznica, iloraz, kwadrat pierwszej liczby, kwadrat drugiej liczby, pierwiastek pierwszej liczby, pierwiastek drugiej liczby wynoszą: "
        ,suma, roznica, iloraz, kwadrat1, kwadrat2, pierwiastek1, pierwiastek2
    )

    if iloczyn == 10: 
        print("iloczyn wynosi ", iloczyn, "Yay!")
    else:
        print("iloczyn wynosi ", iloczyn)