def nwd_odejmowanie(a, b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a

def nwd_dzielenie(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def nww(a, b):
    iloczyn = a * b
    nwd = nwd_dzielenie(a, b)
    return iloczyn // nwd

def skroc_ulamek(licznik, mianownik):
    if mianownik == 0:
        print("Mianownik nie może być zerem!")
    nwd = nwd_dzielenie(abs(licznik), abs(mianownik))
    return licznik // nwd, mianownik // nwd

def formatuj_ulamek(licznik, mianownik):
    if abs(licznik) >= mianownik:
        calosc = licznik // mianownik
        reszta_licznik = abs(licznik) % mianownik
        if reszta_licznik == 0:
            return str(calosc)
        return f"{calosc} {reszta_licznik}/{mianownik}"
    return f"{licznik}/{mianownik}"

def dodaj_ulamki(l1, m1, l2, m2):
    nowy_mianownik = nww(m1, m2)
    mnoznik1 = nowy_mianownik // m1
    mnoznik2 = nowy_mianownik // m2
    nowy_licznik = l1 * mnoznik1 + l2 * mnoznik2
    return skroc_ulamek(nowy_licznik, nowy_mianownik)

def odejmij_ulamki(l1, m1, l2, m2):
    nowy_mianownik = nww(m1, m2)
    mnoznik1 = nowy_mianownik // m1
    mnoznik2 = nowy_mianownik // m2
    nowy_licznik = l1 * mnoznik1 - l2 * mnoznik2
    return skroc_ulamek(nowy_licznik, nowy_mianownik)

def pomnoz_ulamki(l1, m1, l2, m2):
    nowy_licznik = l1 * l2
    nowy_mianownik = m1 * m2
    return skroc_ulamek(nowy_licznik, nowy_mianownik)

def podziel_ulamki(l1, m1, l2, m2):
    if l2 == 0:
        print("Nie można dzielić przez zero!")
    nowy_licznik = l1 * m2
    nowy_mianownik = m1 * l2
    return skroc_ulamek(nowy_licznik, nowy_mianownik)
print(f"wynik nww: {nww(32, 44)}")
print(f"wynik nwd: {nwd_odejmowanie(32, 44)}")
u1 = (-3, 4)
u2 = (4, 6)

print(f"Pierwszy ułamek: {formatuj_ulamek(u1[0], u1[1])}")
print(f"Drugi ułamek: {formatuj_ulamek(u2[0], u2[1])}")

wynik_dodawania = dodaj_ulamki(u1[0], u1[1], u2[0], u2[1])
print(f"Dodawanie: {formatuj_ulamek(u1[0], u1[1])} + {formatuj_ulamek(u2[0], u2[1])} = {formatuj_ulamek(wynik_dodawania[0], wynik_dodawania[1])}")

wynik_odejmowania = odejmij_ulamki(u1[0], u1[1], u2[0], u2[1])
print(f"Odejmowanie: {formatuj_ulamek(u1[0], u1[1])} - {formatuj_ulamek(u2[0], u2[1])} = {formatuj_ulamek(wynik_odejmowania[0], wynik_odejmowania[1])}")

wynik_mnozenia = pomnoz_ulamki(u1[0], u1[1], u2[0], u2[1])
print(f"Mnożenie: {formatuj_ulamek(u1[0], u1[1])} * {formatuj_ulamek(u2[0], u2[1])} = {formatuj_ulamek(wynik_mnozenia[0], wynik_mnozenia[1])}")

wynik_dzielenia = podziel_ulamki(u1[0], u1[1], u2[0], u2[1])
print(f"Dzielenie: {formatuj_ulamek(u1[0], u1[1])} / {formatuj_ulamek(u2[0], u2[1])} = {formatuj_ulamek(wynik_dzielenia[0], wynik_dzielenia[1])}")