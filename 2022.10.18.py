"""
import random
szam=int(input(f"Kérlekk add meg a számot, amire gondoltál (1-től 100-ig)"))
tipp=random.randint(1,100)
lepes=1
if szam<1 or szam>100:
    print(f"Kérlek 1-től 100-ig adj meg számot.")
print ("A gép erre gondolt:", tipp)
while tipp!=szam:
    if tipp>szam:
        tipp-=1
        tipp=random.randint(1, tipp)
        lepes+=1
    else:
        lepes+=1
        tipp=random.randint(tipp, 100)
    print ("A gép erre gondolt:", tipp)
print ("A gép erre gondolt:", tipp, "és helyes volt,", lepes, "lépésből találta ki.")
"""


"""
#1. feladat
elso=int(input(f"Kérlek add meg az első gondolt számot."))
masodik=int(input(f"Kérlek add meg add meg a második gondolt számot."))

print(f"A megoldás:{elso+2*masodik}")
"""


"""
#2. feladat
szam=int(input(f"Kérlek add meg a számot: "))
db=0

while szam!=0:
    if szam>5:
        db+=1
    szam=int(input(f"Kérlek add meg a számot: "))
print(f"Kiléptem a ciklusból: {db}")
"""


"""
#3. feladat
homerseklet=int(input(f"Kérlek add meg a hőmérsékleti adatot: "))
osszeg=0
db=0
atlag=0

while homerseklet>0:
    homerseklet=int(input(f"Kérlek add meg a hőmérsékleti adatot: "))
    osszeg+=homerseklet
    db+=1
if db!=0:
    atlag=round((osszeg/db),1)
print(f"Az átlag hőmérséklet= {atlag}")
"""


"""
#4. feladat
homerseklet=int(input(f"Kérlek adj meg egy hőmérsékleti adatot: "))
db=1

while homerseklet>-5:
    homerseklet=int(input(f"Kérlek adj meg egy hőmérsékleti adatot: "))
    if homerseklet>10:
        db+=1
print(f"{db} darab 10 foknál magasabb hőmérsékletet adtál meg.")
"""


"""
#5. feladat
szam=int(input(f"Kérlek adj meg egy számot: "))
paros=0
paratlan=0

while szam!=0:
    if szam%2:
        szam=int(input(f"Kérlek adj meg egy számot: "))
        paratlan+=1
    else:
        szam=int(input(f"Kérlek adj meg egy számot: "))
        paros+=1
print(f"{paros}db páros számot és {paratlan}db páratlan számot adtál meg.")
"""


"""
#6. feladat
szam=int(input(f"Kérlek adj meg egy számot: "))
osszeg=szam

while szam!=0:
    szam=int(input(f"Kérlek adj meg egy számot: "))
    osszeg+=szam
print(f"{osszeg} a számok összege.")
"""


"""

#7. feladat
szam=int(input(f"Kérlek adj meg egy számot: "))
eredmeny=szam

while szam!=1:
    szam=int(input(f"Kérlek adj meg egy számot: "))
    eredmeny=szam*eredmeny
print(f"A számok szorzata: {eredmeny}")
"""


"""
#8. feladat
penz=2000000
p=int(input(f"Kérlek add meg a kamat százalékát: "))
ev=3
kamatospenz=penz*(((p/100)+1)**ev)

print(f"{kamatospenz} pénzünk lesz három év múlva.")
"""

"""
#9. feladat
?
"""


"""
#10. feladat
n=int(input(f"Sorok száma: "))
m=int(input(f"Oszlopok száma: "))
i=0

while i<n:
    j=0
    while j<m:
        print("*", end="\t")
        j+=1
    print()
    i+=1
i=1
while i<11:
    j=1
    while j<11:
        print(i*j, end="\t")
        j+=1
    print()
    i+=1
"""