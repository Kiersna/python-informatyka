def suma_cyfr(a):
    cyfry = []
    wynik = 0
    while(a != 0):
        cyfra = a % 10
        wynik += cyfra
        a = a // 10
    return wynik


def czy_pierwsza(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def super_pierwsza(poczatek, koniec):
    ile = 0
    for i in range(poczatek, koniec):
        if czy_pierwsza(i) and czy_pierwsza(suma_cyfr(i)):
           ile += 1
    return ile
print("super liczby: ")
print(super_pierwsza(2, 1000))
print(super_pierwsza(100, 10000))
print(super_pierwsza(1000, 100000))

def zamiana_na_binarna(a):
    reszta = a % 2
    a = a//2
    wynik = reszta
    mnoznik = 10
    while a > 0:
        reszta = a % 2
        a = a//2
        wynik = reszta * mnoznik + wynik
        mnoznik *= 10
    return wynik

def superB(poczatek, koniec):
    ile = 0
    for i in range(poczatek, koniec):
        if czy_pierwsza(i) and czy_pierwsza(suma_cyfr(i)) and czy_pierwsza(suma_cyfr(zamiana_na_binarna(i))):
           ile += 1
    return ile
print("superB")
print(superB(2, 1000))
print(superB(100, 10000))
print(superB(1000, 100000))

