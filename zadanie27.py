def niemalejacy(T):
    n = len(T)
    for i in range(n - 1):
        if T[i] <= T[i + 1]:
            return False
    return True
#[5, 4, 3, 2, 1]
print(niemalejacy([3, 4, 5, 5, 7, 9]))

def nierosnacy(T):
    n = len(T)
    for i in range(n - 1):
        if T[i] <= T[i + 1]:
            return False
    return True

print(nierosnacy([3, 2, 1, 0]))

def rosnacy(T):
    n = len(T)
    for i in range(n - 1):
        if T[i] > T[i + 1]:
            return False
    return True

print(rosnacy([3, 4, 5, 5, 7, 9]))

def malejacy(T):
    n = len(T)
    for i in range(n - 1):
        if T[i] < T[i + 1]:
            return False
    return True

print(malejacy([3, 2, 1, 0]))

def staly(T):
    n = len(T)
    for i in range(n - 1):
        if T[i] != T[i + 1]:
            return False
    return True
def jaki_ciag(T):
    n = len(T)
    rosnacy1 = rosnacy(T)
    malejacy1 = malejacy(T)
    nierosnacy1 = nierosnacy(T)
    niemalejacy1 = niemalejacy(T)
    staly1 = staly(T)
    if (rosnacy1 and malejacy1) or (rosnacy1 and nierosnacy1) :
        print("niemotononiczy")
        return
    if staly1:
        print("staly")
        return
    if rosnacy1:
        print("rosnacy")
        return
    if malejacy1:
        print("malejacy")
        return
    if nierosnacy1:
        print("nierosnacy")
        return
    if niemalejacy1:
        print("niemalejacy")
        return
jaki_ciag([1, 2, 3, 4, 5]) #rosnacy
jaki_ciag([5, 4, 3, 2, 1]) #malejacy
jaki_ciag([5, 4, 3, 3, 1]) #nierosnacy
jaki_ciag([1, 2, 3, 3])  #niemalejacy
jaki_ciag([0, 0, 0]) #staly
jaki_ciag([1, 2, 3, 2, 1]) #niemotononiczny
