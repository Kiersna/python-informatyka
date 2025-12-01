def sprawdz_dlugosc(slowo):
    dlugosc = 0
    for i in slowo:
        dlugosc += 1
    return dlugosc
def male_litery(slowo):
    duze = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    male = "abcdefghijklmnopqrstuvwxyz"

    result = ""
    for znak in slowo:
        if znak in duze:
            result += male[duze.index(znak)]
        else:
            result += znak
    return result
def bez_spacji(s):
    spacja = " "
    result = ""
    for znak in s:
        if znak == spacja:
            result += ""
        else:
            result += znak
    return result
def czy_palindrom(s):
    s = male_litery(s)
    s = bez_spacji(s)
    dl = sprawdz_dlugosc(s)
    i = 0
    for i in range(i<dl/2):
        if s[i] != s[dl-1-i]:
            return False
    return True

print(czy_palindrom("12344321"))
print(czy_palindrom("12344322"))
print(czy_palindrom("Oko w oko"))


def czy_palindrom_liczba(liczba):
    dl = len(str(liczba))
    i = 0
    for i in range(i<dl/2):
        if liczba[i] != liczba[dl-1-i]:
            return False
    return True
def zadanie2(liczba):
    while(czy_palindrom_liczba(liczba) == False):
        liczba2 = liczba[::-1]
        liczba = liczba2+liczba
    return liczba

print(zadanie2(195))

