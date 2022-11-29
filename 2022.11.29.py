import random

"""
lista=[]
for i in range(12):
    lista.append(random.randint(-20,20))
print(lista)
print(max(lista)-min(lista))

szamok=[]
for i in range(10):
    szamok.append(random.randint(1,100))
print(len([x for x in szamok if x%2==0]))

db=0
for elem in szamok:
    if elem%2==0:
        db+=1
print(db)
print(sum(szamok))
print(max(szamok))
print(sorted(szamok)[-2])


osszeg=0
nap=0
while osszeg<=100:
    km=int(input("km:"))
    osszeg+=km
    nap+=1
print("Gratuálok! Elérted a célt! Megtettél 100km-t!")
print(f"{osszeg-100} km-rel túlteljesítetted a tervet!")
print(f"A túrát {nap} nap alatt teljesítetted!")
"""


"""
nevek=[]

for i in range(3):
    nevek.append(input())
print(nevek)
space=0
db=[]
for nev in nevek:
    space=0
    for betu in nev:
        if betu==" ":
            space+=1
    if space==2:
        db.append(nev)
print(len(db))

hossz=[]
for nev in nevek:
    hossz.append(len(nev))
maxhossz=max(hossz)
for i in nevek:
    if len(i)==maxhossz:
        print(i)
"""


"""
verseny=[]
print("Adj meg egy nevet és hány km-ig futott: ")
for i in range(5):
    verseny.append((input(""),int(input())))
print(verseny)
print(verseny[1][1])
km=[verseny[0][1]]
for i in range(len(verseny)-1):
    km.append(verseny[i+1][1]-verseny[i][1])
print(km)

maxkm=max(km)
maxii=0
for i in range(len(km)):
    if km[i]==maxkm:
        maxii=i
print(verseny[maxii])
"""

import datetime
DATUM=datetime.date.fromisoformat("2022-11-29")
termek=[]
for i in range(5):
    termeknev=input()
    lejar=datetime.date.fromisoformat(input())
    termek.append((termeknev,lejar))
print(termek)
for t, l in termek:
    if l<DATUM:
        print(t)