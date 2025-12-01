def zadanie1():
    plik = open('slowa.txt', 'r')
    plik2 = open('hasla_a.txt', 'w')
    lines = plik.readlines()
    najdluzsze = len(lines[0])
    najkrotsze = len(lines[0])
    for i in lines:
        i = i[::-1]
        if len(i) > najdluzsze:
            najdluzsze = len(i)
            najdluzsze_slowo = i
        if len(i) < najkrotsze:
            najkrotsze = len(i)
            najkrotsze_slowo = i
        plik2.write(i)
    plik.close()
    plik2.close()
    print(f"Najdluzsze slowo to: {najdluzsze_slowo}, ma {najdluzsze} liter. Najkrotsze slowo to {najkrotsze_slowo}, ma {najkrotsze} liter")

zadanie1()

def zadanie2():
    plik = open('slowa.txt', 'r')
    plik2 = open('hasla_b.txt', 'w')
    lines = plik.readlines()
    index = -1
    index2 = 0
    tablica = []
    for i in lines:
        for j in range(len(i)):
            tablica.append(i[0:index2])
            index2+=1
        for k in tablica:
            index+=1
            if k == k[::-1]:
                najdluzszy_palindrom = k
        slowo_bez_palindromu = i[index:]
        odwrocone = slowo_bez_palindromu[::-1]
        print(odwrocone+najdluzszy_palindrom+slowo_bez_palindromu)

zadanie2()