def suma(p, A, B):
    n = max(len(A), len(B))
    A = A + [0] * (n - len(A))
    B = B + [0] * (n - len(B))

    R = [0] * (n + 1)
    C = [0] * (n + 1)
    A[::-1]
    for i in range(n):
        c = A[i] + B[i] + R[i]
        C[i] = c % p
        R[i + 1] = c // p

    C[n] = R[n]

    while len(C) > 1 and C[-1] == 0:
        C.pop()

    return C

def wynik_do_str(C):
    return ''.join(str(d) for d in reversed(C))

p = 4
A = [2, 2, 1, 3]
B = [1, 2]

C = suma(p, A, B)
print(wynik_do_str(C))