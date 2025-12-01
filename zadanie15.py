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

class Ulamek:
    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            print("Mianownik nie może być zerem!")
        self.licznik = licznik
        self.mianownik = mianownik
        self.skroc()

    def skroc(self):
        nwd = nwd_dzielenie(abs(self.licznik), abs(self.mianownik))
        self.licznik = self.licznik // nwd
        self.mianownik = self.mianownik // nwd
        return self

    def tekst(self):
        if abs(self.licznik) >= self.mianownik:
            calosc = self.licznik // self.mianownik
            reszta_licznik = abs(self.licznik) % self.mianownik
            if reszta_licznik == 0:
                return str(calosc)
            return f"{calosc} {reszta_licznik}/{self.mianownik}"
        return f"{self.licznik}/{self.mianownik}"

    def dodaj(self, inny):
        nowy_mianownik = nww(self.mianownik, inny.mianownik)
        mnoznik1 = nowy_mianownik // self.mianownik
        mnoznik2 = nowy_mianownik // inny.mianownik
        nowy_licznik = self.licznik * mnoznik1 + inny.licznik * mnoznik2
        return Ulamek(nowy_licznik, nowy_mianownik)

    def odejmij(self, inny):
        nowy_mianownik = nww(self.mianownik, inny.mianownik)
        mnoznik1 = nowy_mianownik // self.mianownik
        mnoznik2 = nowy_mianownik // inny.mianownik
        nowy_licznik = self.licznik * mnoznik1 - inny.licznik * mnoznik2
        return Ulamek(nowy_licznik, nowy_mianownik)

    def pomnoz(self, inny):
        nowy_licznik = self.licznik * inny.licznik
        nowy_mianownik = self.mianownik * inny.mianownik
        return Ulamek(nowy_licznik, nowy_mianownik)

    def podziel(self, inny):
        if inny.licznik == 0:
            print("Nie można dzielić przez zero")
        nowy_licznik = self.licznik * inny.mianownik
        nowy_mianownik = self.mianownik * inny.licznik
        return Ulamek(nowy_licznik, nowy_mianownik)

# Przykłady użycia:
u1 = Ulamek(1, 3)
u2 = Ulamek(2, 7)
wynik = u1.dodaj(u2)
print(f"{u1.tekst()} + {u2.tekst()} = {wynik.tekst()}")
u3 = Ulamek(5, 6)
u4 = Ulamek(3, 4)
wynik = u3.dodaj(u4)
print(f"{u3.tekst()} + {u4.tekst()} = {wynik.tekst()}")

print(f"Odejmowanie: {u3.tekst()} - {u4.tekst()} = {u3.odejmij(u4).tekst()}")
print(f"Mnożenie: {u3.tekst()} * {u4.tekst()} = {u3.pomnoz(u4).tekst()}")
print(f"Dzielenie: {u3.tekst()} / {u4.tekst()} = {u3.podziel(u4).tekst()}")