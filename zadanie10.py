liczba = int(input("Podaj Liczbe: "))
minimum = liczba
max = liczba
while True:
    liczba = int(input("Podaj liczba lub 0 "))
    if liczba == 0:
        break
    if liczba < minimum:
        minimum = liczba
    if liczba > max:
        max = liczba
print("Minimalna wartość to:", minimum)
print("Maksymalna wartość to:", max)