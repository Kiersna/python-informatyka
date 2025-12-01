def metodaZachlanna(money):
    if money > 500:
        ilosc500 = money // 500
        money -= ilosc500
    if money > 200:
        ilosc200 = money // 200
        money -= ilosc200
    if money > 100:
        ilosc100 = money // 100
        money -= ilosc100
    if money > 50:
        ilosc50 = money // 50
        money -= ilosc50
    if money > 20:
        ilosc20 = money // 20
        money -= ilosc20
    if money > 10:
        ilosc10 = money // 10
        money -= ilosc10
    if money > 5:
        ilosc5 = money // 5
        money -= ilosc5
    if money > 2:
        ilosc2 = money // 2
        money -= ilosc2
    if money > 1:
        ilosc1 = money // 1
        money -= ilosc1
    return 