import string

def szyfrowanie(k):
    k = k % 26
    slowo_po_zmianie = ''
    wyniki1 = open('wyniki1cezar.txt', 'w')
    with open('dane_6_1.txt', 'r') as plik:
        for line in plik:
            for litera in line:
                x = ord(litera)+k
                if x > 90:
                    roznica = x - 91
                    x = 65+roznica
                litera = chr(x)
                slowo_po_zmianie += litera
            wyniki1.write(slowo_po_zmianie)
szyfrowanie(107)

def deszyfrowanie():

    wyniki = open('wyniki2cezar.txt', 'w')
    with open('dane_6_2.txt', 'r') as plik:
        for line in plik:
            slowo = line.split()
            if len(slowo)<2:
                continue
            k = int(slowo[1])
            k = k % 26
            slowo_po_zmianie = ''
            for litera in slowo[0]:
                x = ord(litera)-k
                if x < ord('A'):
                    x += 26
                litera = chr(x)
                slowo_po_zmianie += litera
            wyniki.write(slowo_po_zmianie+"\n")
deszyfrowanie()