l = [2, 3, 5, 7]
l2 = {1, 2, 3, 4}
def metoda(lista):
    w = 0
    while len(lista) > 1:
        x = min(lista)
        lista.remove(x)
        y = min(lista)
        lista.remove(y)
        z = x+y
        w += z
        lista.append(z)
        print(lista, w)
    return lista, w
#metoda([2, 3, 5, 7])

def metoda2(lista):
    def dlugosc(lista):
        licznik = 0
        for i in lista:
            licznik += 1
        return licznik
    pierwsza = 0
    druga = 0
    idxP = 0
    idxD = 0
    licznik = 0
    koszt = 0
    while dlugosc(lista) > 0:
        for i in lista:
            licznik += 1
            if i < pierwsza:
                pierwsza = i
                idxP = licznik
                continue
            if i < druga :
                druga = i
                idxD = licznik
        del lista[idxP]
        del lista[idxD]
        sumaDwoch = pierwsza + druga
        lista = lista + sumaDwoch
        koszt += sumaDwoch
    return koszt

print(metoda2(l))