from math import sqrt
def sito(n):
    sito = [True]*(n+1)
    sito[0] = sito[1] = False
    for i in range(2, n):
        sito[i] = True
    for i in range(2, int(sqrt(n)+1)):
        if sito[i] == True:
            j = i*i
            while j<= n:
                sito[j] = False
                j = j+i
    pierwsze = []
    for i in range(2, n+1):
        if sito[i]:
            pierwsze.append(i)
    return pierwsze
print(sito(15))

def czy_pierwsza(n):
    if sito(n):
        return True
    return False

print(czy_pierwsza(97))