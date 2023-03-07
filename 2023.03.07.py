"""
class Csoport():
    def __init__(self,s):
        sor=s.split(";")
        self.nev=sor[0]
        self.magassag=int(sor[1])
lista=[]
with open("csoport.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Csoport(i.strip()))
f.close()
for i in lista:
    print(f"{i.nev} - {i.magassag}")
print(lista[0].nev)

#1. feladat: Mennyi az átlag magasság?
osszeg=0
for i in lista:
    osszeg+=i.magassag
atlag=round(osszeg/len(lista))
print(f"{atlag}cm az átlag magasság.")
#2. feladat: Ki a legmagasabb?
max_magassag=lista[0].magassag
maxi=0
for index in range(len(lista)):
    if lista[index].magassag>max_magassag:
        max_magassag=lista[index].magassag
        maxi=index
print(f"Legmagasabb ember: {lista[maxi].nev}, magassága: {lista[maxi].magassag}cm")
"""

"""
lista=[]
f=open('gyumi.txt', "r", encoding="utf-8")
ki=open('csillag.txt', "w", encoding="utf-8")
while True:
    betu=f.read(1)
    dbE=0
    dbe=0
    if betu:
        if betu=="E" or betu=="e":
            ki.write("*")
            if betu=="E":
                dbE+=1
            elif betu=="e":
                dbe+=1
        else:
            ki.write(betu)
    else:
        break
f.close()
ki.close()
(f"E-betűk száma: {dbE}, e-betűk száma: {dbe}")
"""

"""
lista=f.readlines()
uj=[]
for i in lista:
    uj.append(i.strip())
print(uj)
"""

"""
for sor in f:
    lista.append(sor.strip())
f.close
print(lista)
"""

"""
class Eu():
    def __init__(self,s):
        sor=s.split(";")
        self.orszag=sor[0]
        self.datum=sor[1]
lista=[]
with open("eu.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Eu(i.strip()))
f.close()
#print(lista[0].orszag)

for i in lista:
    if "ország" in i.orszag:
        print(i.orszag)

#Szerepel-e Magyarország a listában?
van=False
for i in lista:
    if "Magyarország" in i.orszag:
        van=True
    else:
        van=False
print("Benne van Magyarország a listában." if van==True else "Nincs benne Magyarország a listában.")
"""

"""
class Prognyelv():
    def __init__(self,s):
        sor=s.split(";")
        self.evszam=sor[0]
        self.prognyelv=sor[1]
        self.keresztnev=sor[2]
        self.csaladnev=sor[3]
lista=[]
with open ("forrasfajl.csv", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Prognyelv(i.strip()))
f.close()
"""