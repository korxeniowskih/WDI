#Należy napisać program, który umożliwia zmianę nazw, kopiowanie,
# przenoszenie i usuwanie plików zgodnie z życzeniem użytkownika. 
# Można skorzystać z modułu os. Program powinien poprosić użytkownika o hasło
# a następnie porównać je z zahashowanym hasłem 
# znajdującym się w pliku /home/my_hashed_password.txt.
# Należy skorzystać z modułu hashlib. Należy obsłużyć niezbędne wyjątki.

import os
import hashlib


def obsluga_wyjatkow(operacja):
    try:
        operacja()
    except FileExistsError:
        print("Plik o podanej nazwie już istnieje.")
    except FileNotFoundError:
        print("Nie znaleziono wskazanego pliku.")
    except PermissionError:
        print("Brak uprawnień do wykonania operacji.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")


def zmien_nazwe_pliku():
    aktualna_sciezka = input("Podaj aktualną ścieżkę do pliku: ")
    nowa_sciezka = input("Podaj nową nazwę pliku lub ścieżkę: ")
    os.rename(aktualna_sciezka, nowa_sciezka)
    print("Nazwa pliku została zmieniona.")


def skopiuj_plik():
    sciezka_zrodlowa = input("Podaj ścieżkę do pliku źródłowego: ")
    sciezka_docelowa = input("Podaj ścieżkę docelową dla pliku: ")
    with open(sciezka_zrodlowa, "rb") as plik_zrodlo:
        with open(sciezka_docelowa, "wb") as plik_cel:
            while fragment := plik_zrodlo.read(4096):  # Operator walrus, odczyt fragmentów
                plik_cel.write(fragment)
    print("Plik został skopiowany.")


def usun_plik():
    sciezka_do_pliku = input("Podaj ścieżkę do pliku, który chcesz usunąć: ")
    os.remove(sciezka_do_pliku)
    print("Plik został usunięty.")


def przenies_plik():
    sciezka_zrodlowa = input("Podaj ścieżkę do pliku źródłowego: ")
    sciezka_docelowa = input("Podaj nową ścieżkę docelową: ")
    os.rename(sciezka_zrodlowa, sciezka_docelowa)
    print("Plik został przeniesiony.")


# Wczytanie zahashowanego hasła z pliku
try:
    with open("home/my_hashed_password.txt", "r") as plik:
        zahashowane_haslo = plik.readline().strip()
except FileNotFoundError:
    print("Nie znaleziono pliku z hasłem.")
    exit(1)

# Walidacja hasła użytkownika
while True:
    podane_haslo = input("Podaj hasło: ")
    hash_md5 = hashlib.md5(podane_haslo.encode()).hexdigest()
    if hash_md5 == zahashowane_haslo:
        print("Hasło poprawne. Dostęp przyznany.")
        break
    else:
        print("Błędne hasło. Spróbuj ponownie.")

# Główna pętla programu
while True:
    print("\nDostępne operacje:")
    print("1. Kopiowanie pliku")
    print("2. Przenoszenie pliku")
    print("3. Zmiana nazwy pliku")
    print("4. Usuwanie pliku")
    print("5. Wyjście")

    wybor = input("Wybierz operację (1-5): ")

    if wybor == "1":
        obsluga_wyjatkow(skopiuj_plik)
    elif wybor == "2":
        obsluga_wyjatkow(przenies_plik)
    elif wybor == "3":
        obsluga_wyjatkow(zmien_nazwe_pliku)
    elif wybor == "4":
        obsluga_wyjatkow(usun_plik)
    elif wybor == "5":
        print("Zamykanie programu")
        break
    else:
        print("Nieprawidłowy wybór. Proszę spróbować ponownie.")
