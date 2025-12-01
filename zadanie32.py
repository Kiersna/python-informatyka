def sortuj(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n -i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
def check(s1, s2):
    #posortowane funkcją sorted stringi są porównywane
    s1 = list(s1)
    s2 = list(s2)
    if(sortuj(s1)== sortuj(s2)):
        print("Stringi są anagramami.")
    else:
        print("Stringi nie są anagramami")
#wywołanie
s1 ="listen"
s2 ="silent"
check(s1, s2)


def check2(s1 , s2):
    slowo1 = list(s1)
    slowo2 = list(s2)
    if(len(slowo1) != len(slowo2)):
        return False
    licz = [0]*127
    for i in range(0, len(slowo1)):
        licz[ord(slowo1[i])] += 1
    for i in range(0 , len(slowo2)):
        licz[ord(slowo2[i])] += -1
    for i in range(127):
        if licz[i] != 0:
            return False
    return True

print(check2("listen", "silent"))

def check2_dict(s1, s2):
    if len(s1) != len(s2):
        return False
    licz = {}
    for ch in s1:
        if ch in licz:
            licz[ch] += 1
        else:
            licz[ch] = 1
    for ch in s2:
        if ch in licz:
            licz[ch] -= 1
        else:
            licz[ch] = -1
    for klucz in licz:
        if licz[klucz] != 0:
            return False
    return True


print(check2_dict("pozdro", "podrzo"))
