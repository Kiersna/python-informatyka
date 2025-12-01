import random

def losowe_calkowite_a():
    return random.randint(-15, 15)

def losowe_rzeczywiste_b():
    return round(random.uniform(1.5, 2.25), 2)

def losowe_rzeczywiste_c():
    return round(random.uniform(0, 1), 2)

def losowe_ciag_calkowitych_d():
    lista = []
    for i in range(6):
        lista.append(random.randint(3, 25))
    return lista

def losowe_ciag_rzeczywistych_e():
    lista = []
    for i in range(4):
        lista.append(round(random.uniform(0, 64.5), 1))
    return lista

print(losowe_calkowite_a())
print(losowe_rzeczywiste_b())
print(losowe_rzeczywiste_c())
print(losowe_ciag_calkowitych_d())
print(losowe_ciag_rzeczywistych_e())