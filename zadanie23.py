#p<10; 10 na p; p na 10; 16tkowy
#rzymskie na 10 i odwrotnie

def dziesietny_na_system(liczba, system):
    liczba_w_systemie = 0
    mnoznik = 1
    while(liczba>0):
        cyfra = liczba % system
        liczba = liczba // system
        liczba_w_systemie += mnoznik * cyfra
        mnoznik *= 10
    print(liczba_w_systemie)

dziesietny_na_system(18, 2);

def system_na_dziesietny(liczba, system):
    potega = 0
    wynik = 0
    while(liczba>0):
        cyfra = liczba % 10
        wynik += cyfra * (system**potega)
        potega += 1
        liczba = liczba // 10
    print(wynik)

system_na_dziesietny(10010, 2)

def dziesietny_na_system_do_16(liczba, system):
    cyfry = "0123456789ABCDEF"
    liczba_w_systemie = ""

    while(liczba>0):
        cyfra = cyfry[liczba % system]
        liczba = liczba // system
        liczba_w_systemie =  cyfra + liczba_w_systemie
    print(liczba_w_systemie)

dziesietny_na_system_do_16(32222, 16);

def system_na_dziesietny_do_16(liczba, system):
    cyfry = "0123456789ABCDEF"
    wynik = 0
    potega = 0

    for znak in reversed(liczba):
        cyfra = cyfry.index(znak)
        wynik += cyfra * (system ** potega)
        potega += 1

    print(wynik)
system_na_dziesietny_do_16("A123", 10)


def lista(liczba):
    w = []
    while(liczba > 0):
        w = [liczba % 2]+w
        liczba //= 2
    print(w)

lista(23)

def to_system(n, base):
    if n == 0:
        return ("0")
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ"
    wynik = ''
    while n>0:
        wynik = digits[n % base] + wynik
        n //= base
    return wynik
