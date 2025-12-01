def metodaZachlanna(do_wydania):
    nominaly = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    wydane = {}

    for nominal in nominaly:
        if do_wydania >= nominal:
            ilosc = int(do_wydania // nominal)
            wydane[nominal] = ilosc
            do_wydania = round(do_wydania - ilosc * nominal, 2)

    return wydane

def wypiszWynik(wydane):
    for nominal, ilosc in wydane.items():
        print(f"{nominal} - {ilosc}")


kwota = 111.79
do_wydania = round(kwota, 2)
wydane_nominally = metodaZachlanna(do_wydania)
wypiszWynik(wydane_nominally)