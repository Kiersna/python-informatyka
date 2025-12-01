def zadanie2(do_wydania, brakujace_nominaly):
    nominaly = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    wydane = {}

    print("Brakujące nominały:", brakujace_nominaly)

    for nominal in nominaly:
        if nominal in brakujace_nominaly:
            continue
        if do_wydania >= nominal:
            ilosc = int(do_wydania // nominal)
            if ilosc > 0:
                wydane[nominal] = ilosc
            do_wydania = round(do_wydania - ilosc * nominal, 2)

    if wydane:
        print("Reszta:")
        for nominal, ilosc in wydane.items():
            print(f"{nominal} - {ilosc}")
    else:
        print("Nie wydano żadnej reszty.")

    return wydane

do_wydania = 1200.19
brakujace_nominaly = [200, 10, 0.02]
zadanie2(do_wydania, brakujace_nominaly)