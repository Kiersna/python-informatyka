import math
def f1(x):
    return 2 * x * x + 3 * x - 5
def f2(x):
    return math.cos(x)+2 * math.sin(x)
def f3(x):
    return 2 * x * x * x - x * x + 3 * x - 14
def mce_zerowe_bisekcja(a,b,e,f):
    if f(a) * f(b) > 0:
        return None
    while (b - a) / 2 > e:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

print(mce_zerowe_bisekcja(-1, 2, 0.000001, f1))
print(mce_zerowe_bisekcja(0, 4, 0.000001, f2))
print(mce_zerowe_bisekcja(0, 3, 0.000001, f3))