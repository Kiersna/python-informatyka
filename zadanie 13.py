def silnia(n):
    if n == 0:
        return 1
    s = 1
    for i in range(1, n+1):
        s = s * i
    return s

liczba = 5
s = silnia(liczba)
print("silnia(" , liczba, ") =", s)

def silnia_rek(n):
    if n > 0:
        return n * silnia_rek(n - 1)
    return 1

#plik zadanie 3
def symbol_newtona(n, k):
    if not (0 < k < n):
        return "Nieprawidłowe wartości k lub n"

    wynik = silnia(n) / (silnia(k) * silnia(n - k))
    return int(wynik)
n = 5
k = 2
wynik = symbol_newtona(n, k)
print(f"3. Symbol Newtona ({n}, {k}) =", wynik)
#a
def suma_silni(n):
    suma = 0
    for i in range(1, n + 1):
        suma += silnia(i)
    return suma

n = 5
wynik_sumy = suma_silni(n)
print(f"a) Suma silni od 1! do {n}! = {wynik_sumy}")
#b
def suma_szeregu(n):
    suma = 0
    for i in range(1, n + 1):
        licznik = silnia(i) * (-1)**(i+1)
        mianownik = -0.2 + (i-1) * 0.3
        suma += licznik / mianownik
    return suma

n = 5
wynik_szeregu = suma_szeregu(n)
print(f"b) Suma {n} pierwszych wyrazów szeregu = {wynik_szeregu}")

#c
def oblicz_szereg_c(n):
    licznik = 0
    for i in range(1, n + 1):
        znak = (-1) ** (i + 1)
        wartosc = (n ** 2) / (i * silnia(i))
        licznik += znak * wartosc

    mianownik = 0
    for i in range(1, n + 1):
        mianownik += i / (3 * i)
    if mianownik == 0:
        return "Nie można dzielić przez zero"

    return licznik / mianownik

n = 5
wynik_szeregu_c = oblicz_szereg_c(n)
print(f"c) Wartość szeregu c dla n = {n}: {wynik_szeregu_c}")
