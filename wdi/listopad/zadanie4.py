#Należy napisać program, który umożliwia zmianę nazw, kopiowanie,
# przenoszenie i usuwanie plików zgodnie z życzeniem użytkownika. 
# Można skorzystać z modułu os. Program powinien poprosić użytkownika o hasło
# a następnie porównać je z zahashowanym hasłem 
# znajdującym się w pliku /home/my_hashed_password.txt.
# Należy skorzystać z modułu hashlib. Należy obsłużyć niezbędne wyjątki.

import os 
import hashlib

try:
    with open("home/my_hashed_password.txt","r") as plik:
        hash_hasla = plik.readline()
except FileNotFoundError:
    hash_hasla = input("nie istnieje plik z hashem, wprowadź hash samemu")
while True:
    haslo = input("Podaj hasło")
    sha256 = hashlib.sha256() #
    sha256.update(haslo.encode()) #
    hash = sha256.hexdigest()
    if hash == hash_hasla:
        print("hasło poprawne")
        break
    else:
        print("błędne hasło spróbuj jeszcze raz")     
            
def wyjatki(funkcja):
    try:
        funkcja() 
    except FileExistsError:
        print("istnieje juz plik o tej nazwie")
    except FileNotFoundError:
        print("podano nieistniejacy plik")
    except PermissionError:
        print("brak uprawnien do wykonania operacji")
    except Exception as e:
            print(f"Wystąpił nieoczekiwany błąd: {e}")
        
        
def zmiana_nazwy():
    stara_nazwa = input("podaj ścieżkę źródłową: ")
    nowa_nazwa = input("podaj nowa nazwę pliku: ")
    os.rename(stara_nazwa,nowa_nazwa)
    print("nazwa została zmieniona")
        
def kopiowanie():
    sciezka = input("podaj ścieżkę źródłową: ")
    sciezka_doc = input("podaj ścieżke docelową: ")
    with open(sciezka,"rb") as zrodlo:
        with open(sciezka_doc,"wb") as nowy:
            while chunk := zrodlo.read(4096): #walrus operator, odczytywanie w chunkach w celu unikniecia problemow z pamiecia
                nowy.write(chunk)
    print("plik skopiowano")
    
def usuwanie():
    plik = input("podaj plik do usunięcia: ")
    os.remove(plik)
    print("plik usunięto")
        

def przenoszenie():
    sciezka = input("podaj ścieżkę źródłową: ")
    sciezka_doc = input("podaj ścieżkę docelową: ")
    os.rename(sciezka,sciezka_doc)
    print("nazwa została zmieniona")
        
while True:
    print("\nWybierz operację:")
    print("1. Zmień nazwę pliku")
    print("2. Skopiuj plik")
    print("3. Przenieś plik")
    print("4. Usuń plik")
    print("5. Wyjście")

    print(os.listdir()) 

    choice = input("Wybierz opcję (1-5): ")

    if choice == '1':
        wyjatki(zmiana_nazwy)
    elif choice == '2':
        wyjatki(kopiowanie)
    elif choice == '3':
        wyjatki(przenoszenie)
    elif choice == '4':
        wyjatki(usuwanie)
    elif choice == '5':
        print("Zakończenie programu.")
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")