def kompresja_LZW(dane):
    slownik = {'N':1, 'C':2, 'Z': 3}
    rozm_slow = 4
    p = dane[0]
    wynik = []
    for z in dane[1:]:
        pz = p+z
        if pz in slownik:
            p = pz
        else:
            wynik.append(slownik[p])
            slownik[pz] = rozm_slow
            #slownik.update({pz : rozm_slow})
            p = z
            rozm_slow += 1
    if p != "":
        wynik.append(slownik[p])
    print(slownik)
    return wynik
print(kompresja_LZW("NNNCCCCCCCNNNCCCNZCN"))

#dekompresja i 4.9

def dekompresja(wynik):
    slownik = {1:'N', 2:'C', 3:'Z'}
    rozm_slow = 4
    wynik2 = []
    kod = wynik[0]
    s = slownik[kod]
    wynik2.append(s)
    p = s
    for kod in wynik[1:]:
        if kod in slownik:
            wpis = slownik[kod]
        else:
            wpis = p + p[0]
        wynik2.append(wpis)
        slownik[rozm_slow] = p + wpis[0]
        rozm_slow += 1
        p = wpis
    return "".join(wynik2)
print(dekompresja(kompresja_LZW("NNNCCCCCCCNNNCCCNZCN")))



