def horner_iter(A, x):
    w = A[0]
    for i in range(1, len(A)):
        w = w * x + A[i]
    return w

def horner_rek(A, x, i=0):
    if i == len(A) - 1:
        return A[i]
    return A[i] + x * horner_rek(A, x, i + 1)

def konwersja_iter(liczba, podstawa):
    wynik = 0
    for c in liczba:
        wynik = wynik * podstawa + int(c)
    return wynik

def konwersja_rek(liczba, podstawa, i=0):
    if i == len(liczba) - 1:
        return int(liczba[i])
    return int(liczba[i]) * podstawa + konwersja_rek(liczba, podstawa, i + 1)

def hex_na_10(liczba):
    cyfry = "0123456789ABCDEF"
    liczba = liczba.upper()
    wynik = 0
    for c in liczba:
        wynik = wynik * 16 + cyfry.index(c)
    return wynik

A = [2, 4, -3, 7]
x = 3

print("Wielomian 2x3 + 3x2 - 5x + 7 dla x =", x)
print("Iteracyjnie:", horner_iter(A, x))
print("Rekurencyjnie:", horner_rek(A, x))

print("\nKonwersja 1011 (dwojkowy) na dziesiętny:")
print("Iteracyjnie:", konwersja_iter("1011", 2))
print("Rekurencyjnie:", konwersja_rek("1011", 2))

print("\nKonwersja 143 (osemkowy) na dziesiętny:")
print("Iteracyjnie:", konwersja_iter("143", 8))
print("Rekurencyjnie:", konwersja_rek("143", 8))

print("\n16tkowy na dziesiętny (tylko iter):")
print("FF =", hex_na_10("FF"))
print("1A3 =", hex_na_10("1A3"))
print("CAFE =", hex_na_10("CAFE"))