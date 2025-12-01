def szkolna_metoda(x, n):
    licznik =  0
    wynik = 1
    for i in range(n):
        wynik = wynik*x
        licznik += 1
    return wynik, licznik

print(szkolna_metoda(3, 4))

def potega1(x, n):
    licznik  =  0
    if n == 0:
        return 1
    if n % 2 != 0:
        return x*potega1(x, n-1)
    else:
        a = potega1(x, n/2)
    return a*a

print(potega1(3, 4))
#10 to 6 15 to 8 a 100 to 10 na 2
def potega2(x,n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return x*((potega2(x, (n-1)/2))*(potega2(x, (n-1)/2)))
    return ((potega2(x, n/2))*(potega2(x, n/2)))

print(potega2(3, 4))

def od_prawej_do_lewej(x,  n):
    w = 1
    licznik = 0
    while n>0:
        if n % 2 == 1:
            w = w *x
            licznik += 1
        x = x*x
        licznik +=1
        n = n // 2
    return w, licznik
print(od_prawej_do_lewej(2, 10))
