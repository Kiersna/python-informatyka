def niemalejacy(T):
    for i in range(len(T) - 1):
        if T[i] > T[i + 1]:
            return False
    return True

def nierosnacy(T):
    for i in range(len(T) - 1):
        if T[i] < T[i + 1]:
            return False
    return True

def rosnacy(T):
    for i in range(len(T) - 1):
        if T[i] >= T[i + 1]:
            return False
    return True

def malejacy(T):
    for i in range(len(T) - 1):
        if T[i] <= T[i + 1]:
            return False
    return True

def staly(T):
    for i in range(len(T) - 1):
        if T[i] != T[i + 1]:
            return False
    return True

def jaki_ciag(T):
    if staly(T):
        print("stały")
    elif rosnacy(T):
        print("rosnący")
    elif malejacy(T):
        print("malejący")
    elif niemalejacy(T):
        print("niemalejący")
    elif nierosnacy(T):
        print("nierosnący")
    else:
        print("niemonotoniczny")

jaki_ciag([1, 2, 3, 4, 5])   # rosnący
jaki_ciag([5, 4, 3, 2, 1])   # malejący
jaki_ciag([5, 4, 3, 3, 1])   # nierosnący
jaki_ciag([1, 2, 3, 3])      # niemalejący
jaki_ciag([0, 0, 0])         # stały
jaki_ciag([1, 2, 3, 2, 1])   # niemotononiczy
