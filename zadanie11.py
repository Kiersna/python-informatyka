def znajdz_maksimum(T):
    maksimum = T[0]
    for i in range(1, len(T)):
        if T[i] > maksimum:
            maksimum = T[i]
    return maksimum

def znajdz_minimum(T):
    minimum = T[0]
    for i in range(1, len(T)):
        if T[i] < minimum:
            minimum = T[i]
    return minimum
T = [3, 1, 4, 1, 5, 9, 2, 6]
maksimum = znajdz_maksimum(T)
minimum = znajdz_minimum(T)
print("Maksimum: ", maksimum, "Minimum: ", minimum)