def przestaw(n):
    w = 0
    m = 1
    while n > 0:
        r = n % 100 #34, 0
        a =  r // 10 #3,
        b = r % 10 #4
        n = n // 100 #12
        if a > 0:
            w += a *m+ 10 * b *m
        else:
             w += b *m

    return w

print(przestaw(1000))
print(przestaw(1234))
print(przestaw(1234567))