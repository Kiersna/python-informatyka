def zadanie1():
    dane = open("dane1.1.txt", "r")
    wyniki = open("wyniki1.1.txt", "w")
    for linia in dane:
        liczby = linia.split()
        liczba1 = liczby[0]
        liczba2 = liczby[1]
        iloczyn = int(liczba1) *int(liczba2)
        if iloczyn in range(250, 3500):
            wyniki.write(str(iloczyn)+"\n")
    dane.close()
    wyniki.close()
#zadanie1()
def zadanie2a():
    dane = open("dane1.22.txt", "r")
    wyniki = open("wyniki1.2.txt", "w")
    for linia in dane:
        wyniki.write(linia)
    dane.close()
    wyniki.close()
#zadanie2a()

def zadanie2b():
    dane = open("wyniki1.2.txt", "r")
    wyniki = open("wyniki1.21.txt", "w")
    for linia in dane:
        if(linia[0] == "m"):
            wyniki.write(linia)
    dane.close()
    wyniki.close()
#zadanie2b()
def zadanie2c():
    dane = open("wyniki1.2.txt", "r")
    wyniki = open("wyniki1.22.txt", "w")
    for linia in dane:
        linia = linia.strip()
        if(len(linia) > 8):
            wyniki.write(linia)
    dane.close()
    wyniki.close()
zadanie2c()
def zadanie2d():
    dane = open("wyniki1.22.txt", "r")
    for linia in dane:
        print(linia)
zadanie2d()


# def zadanie3():
#     znaki = {}
#     dane = open("obrazek.txt", "r")
#     wyniki = open("wynik3.txt", "w")
#     for linia in dane:
#         for znak in linia:
#             if not znak.isspace() and znak not in znaki:
#                 znaki[znak] = 1
#             if not znak.isspace():
#                 znaki[znak] += 1
#     for znak, liczba in znaki.items():
#         wyniki.write(znak, liczba)
#     dane.close()
#     wyniki.close()

# zadanie3()