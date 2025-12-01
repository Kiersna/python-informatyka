def najcz_najrz_slownik(lista):
    slownik = {}
    for elem in lista:
        if elem in slownik:
            slownik[elem] += 1
        else:
            slownik[elem] = 1
    pierwszy = True
    for klucz in slownik:
        if pierwszy:
            najczestszy = klucz
            najrzadszy = klucz
            pierwszy = False
        else:
            if slownik[klucz] > slownik[najczestszy]:
                najczestszy = klucz
            if slownik[klucz] < slownik[najrzadszy]:
                najrzadszy = klucz
    print("Najczęściej występuje:", najczestszy, "-", slownik[najczestszy], "razy")
    print("Najrzadziej występuje:", najrzadszy, "-", slownik[najrzadszy], "raz")
    return slownik


print(najcz_najrz_slownik([3, 4, 5, 6, 6, 6, 6, 5, 4, 3, 2]))