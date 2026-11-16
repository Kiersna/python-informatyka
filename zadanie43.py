class Stos:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

s1 = Stos()
s1.push(10)
s1.push(12)
s1.push(14)
s1.size()
s1.peek()
while (s1.isEmpty() == False):
    s1.pop()
s1.isEmpty()
s1.size()
def a1():
    s2 = Stos()
    nawiasy = "(()())"
    for i in nawiasy:
        if i == "(":
            s2.push(i)
        if i == ")":
            if s2.isEmpty():
                return False
            s2.pop()
    if s2.isEmpty():
        return True
print("zad 1: ")
print(a1())

def b1(tekst):
    s3 = Stos()
    otwierajace = ["(", "{", "["]
    # if tekst[0] != "{":
    #     return False
    # if tekst[1] != "[" and tekst[1] != "{":
    #     return False
    def sprawdzenie_hierarchii(tekst):
        znak = ""
        index = 0
        for i in tekst:
            znak = i
            if znak == "[":
                if tekst[index+1] == "{":
                    return False
            if znak == "(":
                if tekst[index+1] == "{" or tekst[index+1] == "[":
                    return False
            index+=1
        return True
    if sprawdzenie_hierarchii(tekst) == False:
        print("zla hierarchia")
        return False
    for i in tekst:
        if i == "{" or i == "[" or i == "(":
            s3.push(i)
        if i == "}" or i == "]" or i == ")":
            if s3.isEmpty() or s3.peek() not in otwierajace:
                return False
            else:
                s3.pop()
    if s3.isEmpty():
        return True
    return False
print("zad 1b: ")
print(b1("{[(())][]}{()}"))

def zad2(liczba):
    s4 = Stos()
    liczbaDwojkowa = []
    while liczba > 0:
        reszta = liczba % 2
        s4.push(reszta)
        liczba = liczba // 2
    while s4.isEmpty() == False:
        liczbaDwojkowa.append(s4.pop())
    return "".join(map(str,liczbaDwojkowa))
    #return liczbaDwojkowa
print("zad2: ")
print(zad2(4))

def zad3():
    StosX = Stos()
    StosY = Stos()
    with open("Dane.txt") as plik:
        StosX.push(0)
        StosY.push(0)
        for i in plik:
            if i[0] == "R":
                StosX.push(i[5])
                StosY.push(i[7])
            if i[0] == "C":
                if StosX.peek() != "0":
                    StosX.pop()
                if StosY.peek() != "0":
                    StosY.pop()
            if i[0] == "P":
                print(f"({StosX.peek()}, {StosY.peek()})")
            if i[0] == "I":
                print(StosX.size())
zad3()

def zad3B():
    StosX = Stos()
    StosY = Stos()
    StosXcof = Stos()
    StosYcof = Stos()
    with open("Dane2.txt") as plik:
        StosX.push(0)
        StosY.push(0)
        for i in plik:
            if i[0] == "R":
                StosX.push(i[5])
                StosY.push(i[7])
            if i[0] == "C":
                if StosX.peek() != "0":
                    StosXcof.push(StosX.peek())
                    StosX.pop()
                if StosY.peek() != "0":
                    StosYcof.push(StosY.peek())
                    StosY.pop()
            if i[0] == "P" and i[2] == "K":
                print(f"({StosX.peek()}, {StosY.peek()})")
            if i[0] == "I":
                print(StosX.size())
            if i[0] == "P" and i[3] == "N":
                if(StosXcof.isEmpty()):
                    print("nie ma ruchu do ponowienia")
                else:
                    StosX.push(StosXcof.pop())
                    StosY.push(StosYcof.pop())
print("zad 3 b: ")
print("")
zad3B()
