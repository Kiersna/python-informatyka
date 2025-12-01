import math
def f1(x):
    return x**3 + 5*x - 3

def f2(x):
    return x**3 - 8

def f3(x):
    return x**2 - 4

def f4(x):
    return x**2 - x - 3

def mce_zerowe_bisekcja(p, q, L, f):
    if f(p) * f(q) > 0:
        return None
    iteracja = 0
    while iteracja < L:
        c = (p + q) / 2
        if f(c) == 0 or (q - p) / 2 < 1e-6:
            return c
        elif f(p) * f(c) < 0:
            q = c
        else:
            p = c
        iteracja += 1
    return (p + q) / 2

print(mce_zerowe_bisekcja(-2, 2, 10, f1))
print(mce_zerowe_bisekcja(0, 4, 12, f2))
print(mce_zerowe_bisekcja(-1, 6, 8, f3))
print(mce_zerowe_bisekcja(0, 8, 11, f4))
