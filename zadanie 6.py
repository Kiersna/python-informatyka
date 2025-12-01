import random

def czy_podzielna_przez_7(n):
    tab = []
    for _ in range(n):
        tab.append(random.randint(1, 100))
    for i in range(n):
        if tab[i] % 7 == 0:
            return True, tab
    return False, tab

def wszystkie_wieksze_od_5(n):
    tab = []
    for _ in range(n):
        tab.append(random.randint(1, 100))
    for num in tab:
        if num <= 5:
            return False, tab
    return True, tab

def czy_rozna_od_2(n):
    tab = []
    for _ in range(n):
        tab.append(random.randint(0, 10))
    for i in range(n):
        if tab[i] != 2:
            return True, tab
    return False, tab

def wszystkie_niepodzielne_przez_4():
    tab = []
    for _ in range(11):
        tab.append(random.randint(0, 32))
    for num in tab:
        if num % 4 == 0:
            return False, tab
    return True, tab

print(czy_podzielna_przez_7(10))
print(wszystkie_wieksze_od_5(10))
print(czy_rozna_od_2(10))
print(wszystkie_niepodzielne_przez_4())