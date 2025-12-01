def odbicia():
    with open("liczby1.txt", "r") as plik:
        linie = plik.read().splitlines()
    odbicia_lista = []
    for i in linie:
        odwrocone = i[::-1]
        odbicia_lista.append(odwrocone)
    plik.close()
    return odbicia_lista

def podzielnePrzez17(odbicia):
    for i in odbicia:
        i = int(i)
        if(i % 17 == 0):
            print(i)

odbiciaLista = odbicia()
podzielnePrzez17(odbiciaLista)

def zadanie4_2():
    with open("liczby1.txt", "r") as plik:
        linie = plik.read().splitlines()
    max_roznica = -1
    liczba_z_max_roznica = None
    for linia in linie:
        liczba = int(linia)
        odbicie_liczba = int(linia[::-1])
        roznica = abs(liczba - odbicie_liczba)
        if roznica > max_roznica:
            max_roznica = roznica
            liczba_z_max_roznica = liczba

    print("Liczba z największą różnicą:", liczba_z_max_roznica)
    print("Największa wartość różnicy:", max_roznica)

def czy_pierwsza(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def zadanie4_3():
    with open("liczby1.txt", "r") as plik:
        linie = plik.read().splitlines()
    for linia in linie:
        liczba = int(linia)
        odbicie_liczba = int(linia[::-1])
        if czy_pierwsza(liczba) and czy_pierwsza(odbicie_liczba):
            print(liczba)

zadanie4_2()
zadanie4_3()