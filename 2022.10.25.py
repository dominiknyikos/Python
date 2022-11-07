#A csoport
"""
#1. feladat
import random

erme= ["Fej", "Írás"]
talalat= random.choice(erme)
valasztas= input(f"Fej vagy Írás válassz: ")

if valasztas==talalat:
    print(f"Eltaláltad, valójában {talalat} volt.")
else:
    print(f"Nem találtad el, valójában {talalat} volt.")
"""


"""
#2. feladat
for szam in range (1,10,2):
    print(szam, end=",")
"""

"""
#3. feladat
alkalom=input(f"Kérlek add meg mikor írjam ki a szöveget: ")
szoveg=input(f"Kérlek add meg a szöveget: ")
utasitas=input(f"Kérlek add meg mikor az indítószót: ")

while alkalom!=utasitas:
    utasitas=input(f"Kérlek add meg mikor az indítószót: ")
else:
    print(szoveg)
"""

"""
#4. feladat
szam=int(input(f"Kérlek adj meg egy számot: "))

while szam%2!=0:
    szam=int(input(f"Kérlek adj meg egy számot: "))
else:
    print(f"Páros számot adtál meg.")
"""


"""
#5. feladat
i=1

while i<6:
    j=1
    while j<6:
        print(i*j, end="\t")
        j+=1
    print()
    i+=1
"""



#B csoport
"""
#1. feladat
[print(i) for i in range(2,11,+2)]
"""


"""
#2. feladat
szo=input(f"Kérlek adj meg valamit: ")
stop="állj"

while szo!=stop:
    szo=input(f"Kérlek adj meg valamit: ")
else:
    print(f"Megállítottál")
"""


"""
#3. feladat
import random
szam = random.randint(1,12)
db=0
oszthato=0

while db!=20:
    if szam%3==0:
        print(szam, end="; ")
        db+=1
        oszthato+=1
        szam= random.randint(1,12)
    else:
        szam= random.randint(1,12)
        db+=1
print(f"\n{oszthato} darab ilyen szám volt")
"""


"""
#4. feladat
n=int(input(f"Sorok száma: "))
m=int(input(f"Oszlopok száma: "))
i=0

while i<n:
    j=0
    while j<m:
        print("o", end="\t")
        j+=1
    print()
    i+=1
"""