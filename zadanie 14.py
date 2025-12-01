def silnia(n):
    if n == 0:
        return 1
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s


def zadanie3(n, k):
    if k < 0 or k > n:
        return "Nieprawidłowe wartości k lub n"

    wynik = silnia(n) / (silnia(k) * silnia(n - k))
    return int(wynik)


def suma_silni(n):
    suma = 0
    for i in range(1, n + 1):
        suma += silnia(i)
    return suma

def suma_szeregu(n):
    suma_licznik = 0
    suma_mianownik = 0
    liczba = -0.2
    znak = 1

    for i in range(1, n + 1):
        silnia = 1
        for j in range(1, i + 1):
            silnia *= j
        suma_licznik += znak * silnia
        znak *= -1

        suma_mianownik += liczba
        liczba += 0.3

    return suma_licznik / suma_mianownik





def oblicz_szereg_c(n):
    licznik = 1
    znak = 1
    for i in range(1, n + 1):
        licznik *= znak * (n**2 / silnia(i))
        znak *= -1

    mianownik = 0
    for i in range(1, n + 1):
        mianownik += i / (3 * i)

    return licznik / mianownik

n = 5
k = 2

print(f"Symbol Newtona ({n}, {k}) =", zadanie3(n, k))
print(f"a) Suma silni od 1! do {n}! =", suma_silni(n))
print(f"b) Suma {n} pierwszych wyrazów szeregu =", suma_szeregu(n))
print(f"c) Wartość szeregu c dla n = {n}:", oblicz_szereg_c(n))