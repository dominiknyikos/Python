"""
#A feladat
#1. feladat
class HegyekMo():
#2. feladat
    def __init__(self,s):
        sor=s.split(";")
        self.nev=sor[0]
        self.hegyseg=sor[1]
        self.magassag=int(sor[2])
lista=[]
fejlec=""
with open("hegyekMo.txt", "r", encoding="utf-8") as f:
    fejlec=f.readline()
    for i in f:
        lista.append(HegyekMo(i.strip()))
f.close()

#3. feladat
print(f"Hegycsúcsok száma: {len(lista)} db")

#4. feladat
hegyek_magassaga=[]
for i in lista:
    hegyek_magassaga.append(i.magassag)
legmagasabb=max(hegyek_magassaga)
print(f"Hegycsúcsok átlagos magassága: {sum(hegyek_magassaga)/len(lista)} m")

#5. feladat
for i in lista:
    if legmagasabb==i.magassag:
        print(f"A legmagasabb hegycsúcs adatai: {i.nev} {i.hegyseg} {i.magassag}")

#6. feladat
magassagertek=int(input("Kérek egy magasságot: "))
van=False
for i in lista:
    if i.hegyseg=="Börzsöny":
        if i.magassag>magassagertek:
            van=True
print(f"Van {magassagertek}m-nél magasabb hegycsúcs a Börzsönyben!" if van==True else f"Nincs {magassagertek}m-nél magasabb hegycsúcs a Börzsönyben!")

#7. feladat
meter=3.280839895
db=0
for i in lista:
    if i.magassag*meter>3000:
        db+=1
print(f"3000 lábnál magasabb hegycsúcsok száma: {db}")

#8. feladat
szotar={}
for i in lista:
    if i.hegyseg in szotar:
        szotar[i.hegyseg]+=1
    else:
        szotar[i.hegyseg]=1
for k,v in szotar.items():
    print(f"{k} - {v}")

#9. feladat
ki=open("Bukk.txt", "w", encoding="utf-8")
ki.write(fejlec)

for i in lista:
    if "Bükk-vidék"==i.hegyseg:
        ki.write(i.nev+":"+str(round(i.magassag*meter,2))+"\n")
ki.close
"""

"""
#B feladat
#1. feladat
class Vedett():
#2. feladat
    def __init__(self,s):
        sor=s.split(";")
        self.nev=sor[0]
        self.ertek=int(sor[1])
        self.ev=int(sor[2])
        self.osztaly=sor[3]
lista=[]
with open("vedett.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Vedett(i.strip()))
f.close()

#3. feladat
print(len(lista))

#4. feladat
osszeg=0
db=0
for i in lista:
    if "madarak"==i.osztaly:
        osszeg+=i.ertek
        db+=1
print(f"Madarak értékeinek átlaga: {round(osszeg/db,1)}")

#5. feladat
ertekek=[]
for i in lista:
    ertekek.append(i.ertek)
legdragabb=max(ertekek)

for i in lista:
    if legdragabb==i.ertek:
        print(i.nev)

#6. feladat
db=0
for i in lista:
    if "hüllők"==i.osztaly:
        db+=1
print(f"Hüllők száma: {db} db")

#7. feladat
hiuz=0
for i in lista:
    if "hiúz"==i.nev:
        hiuz=i.ertek
db=0
for i in lista:
    if hiuz==i.ertek:
        db+=1
print(db)

#8. feladat
fajlnev=input("Fájlnév: ")
van=False
for i in lista:
    if i.nev==fajlnev:
        van=True
print("Védett" if van else "Nem védett")

#9. feladat
nevek_hossz=[]
for i in lista:
    nevek_hossz.append(len(i.nev))
leghosszabb_nev=max(nevek_hossz)
for i in lista:
    if leghosszabb_nev==len(i.nev):
        print(i.nev)
"""