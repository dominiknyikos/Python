"""
#1. feladat
import random
tel_nev=input("Kérlek add meg a településed nevét: ")
ir_szam=int(input("Kérlek add meg az irányítószámodat: "))

def kod(s,szam):
    return s[0:2]+str(szam)+str(random.randint(10,99))
print(kod(tel_nev, ir_szam))
"""


"""
#2. feladat
szoveg=input("Kérlek add meg a szöveged: ")

def valtozo(s):
    s=s.lower()
    betu=s[0]
    karakter=s.count(betu)
    return karakter/len(s)*100
print(f"{valtozo(szoveg):.1f}%")
"""


"""
#3. feladat
import random
lista=[]

def feltoltes():
    for i in range(1,366):
        if 1<=i<=59 or 335<=i<=365:
            lista.append(random.randint(40,70))
        elif 60<=i<=151:
            lista.append(random.randint(180,200))
        elif 152<=i<=243:
            lista.append(random.randint(350,400))
        else:
            lista.append(random.randint(80,120))
feltoltes()
print(lista)
print(f"{sum(lista)*1500}Ft")
print(f"{(sum(lista)*1500)-(365*25000)-(50000000)}Ft")
print(f"A legnagyobb utasszám: {lista.index(max(lista))} fő")
print(f"A legkisebb utasszám: {lista.index(min(lista))} fő")
"""


"""
#4. feladat
szoveg=input("Kérlek adj meg egy szöveget: ")

def tavirat(s):
    s=s.upper()
    s.replace(","," ").replace("!",".").replace("?",".")
    lista=s.split(".")
    uj_szoveg=(" STOP").join(lista)
    return uj_szoveg
print(tavirat(szoveg))
"""


"""
#5. feladat
import random
lista=[]
uj_lista=[]

def binaris():
    n=int(input("Kérlek adj meg egy számot: "))
    for i in range(n):
        lista.append(random.randint(0,1))
    print(f"{lista.count(0)}db 0-ás van benne.")
    print(f"{lista.count(1)}db 1-es van benne.")
    print(f"{lista.count(0)/lista.count(1)*100:.1f}% az arányuk.")
    print(lista)
    for i in lista:
        if i==0:
            i=1
            uj_lista.append(i)
        else:
            i=0
            uj_lista.append(i)
    print(uj_lista)
binaris()
"""


"""
#6. feladat
import random
uj_lista=[]

def beosztas():
    for i in range(16):
        csapat=["A", "B", "C", "D"]
        uj_lista.append(random.choice(csapat))
    print(uj_lista)
beosztas()
"""

#7. feladat (Félkész feladat)
huf=int(input("Kérlek add meg az összeget: "))
euro=int(input("Kérlek add meg az összeget: "))

def vetel(euro):
    if 1<=euro<=100:
        print(euro*355)
    else:
        print(euro*350)
vetel(euro)

def eladas(huf):
    if 1<=euro<=100:
        print(euro*355)
    else:
        print(euro*350)
eladas(huf)