def znajdz_min_max(dane):
    n = len(dane)
    for i in range(0, n - 1, 2):
        if dane[i] < dane[i + 1]:
            dane[i], dane[i + 1] = dane[i + 1], dane[i]
    z = None
    if n % 2 != 0:
        z = dane[-1]
        n -= 1

    if n > 0:
        maks = dane[0]
        for i in range(0, n, 2):
            if dane[i] > maks:
                maks = dane[i]
    else:
        maks = z

    if n > 0:
        minimum = dane[1]
        for i in range(1, n, 2):
            if dane[i] < minimum:
                minimum = dane[i]
    else:
        minimum = z

    if z is not None:
        if z < minimum:
            minimum = z
        if z > maks:
            maks = z

    return minimum, maks

dane1 = [3, 5, 1, 9, 2, 8, 4, 7, 6]
min1, max1 = znajdz_min_max(dane1)
print(f"Dane: {dane1}, Min: {min1}, Max: {max1}")

dane2 = [10, 5, 2, 8, 1, 9, 4, 7]
min2, max2 = znajdz_min_max(dane2)
print(f"Dane: {dane2}, Min: {min2}, Max: {max2}")
