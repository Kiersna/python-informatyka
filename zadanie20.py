def zamiana():
        dane = open("liczby.txt", "r")
        wyniki = open("liczby1_wyniki.txt", "w")
        for linia in dane:
            wyniki.write(str(int(linia.strip(), 2))+"\n")
        dane.close()
        wyniki.close()

zamiana()

def zadanie6a():
        wynik = 0
        dane = open("liczby1_wyniki.txt", "r")
        wyniki = open("zadanie6.txt", "w")
        for linia in dane:
                if int(linia) % 2== 0:
                        wynik += 1
        print(wynik)
zadanie6a()

def zadanie6b():
        dane = open("liczby1_wyniki.txt", "r")
        maks = 0
        for linia in dane:
                if int(linia) > maks:
                        maks = int(linia)
                        maks_bin = bin(int(linia))
        print(maks, maks_bin)
zadanie6b()

def zadanie6c():
        ilosc_9 = 0
        suma = 0
        dane = open("liczby1_wyniki.txt", "r")
        for linia in dane:
                if len(int(linia)) == 9:
                        ilosc_9 += 1
                        suma += int(linia)
        print(bin(suma))
zadanie6c()
