import random

def binarySearch(array, target):
    mini = 0
    maxi = len(array) - 1
    porownania = 0
    sprawdzane_indeksy = []

    while mini <= maxi:
        guess = (mini + maxi) // 2
        porownania += 1
        sprawdzane_indeksy.append(guess)

        if array[guess] == target:
            print(f"Liczba porównań: {porownania}")
            print(f"Sprawdzone indeksy: {sprawdzane_indeksy}")
            print(f"indeks: {guess}")
            return guess
        elif array[guess] < target:
            mini = guess + 1
        else:
            maxi = guess - 1

    print(f"Liczba porównań: {porownania}")
    print(f"Sprawdzone indeksy: {sprawdzane_indeksy}")

    return -1

tab = []
for _ in range(15):
    tab.append(random.randint(0, 20))
tab.sort()
print(tab)
binarySearch(tab, 5)