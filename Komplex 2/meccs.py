print("1. feladat")
class Merkozesek():
    def __init__(self,s):
        sor=s.split(" ")
        self.hazai=sor[0]
        self.vendeg=sor[1]
        self.nap=int(sor[2])
        self.jegy=int(sor[3])
lista=[]
with open("naplo.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Merkozesek(i.strip()))
f.close()

print("2. feladat")
db=0
jegyar=0
for i in lista:
    if "Voros_Rokak"==i.hazai or "Voros_Rokak"==i.vendeg:
        db+=1
        jegyar+=i.jegy
print(f"Mérközések száma: {db}, ezekre a jegyár összesen: {jegyar}Ft.")

print("3. feladat")
nap_min=365
nap_max=0
for i in lista:
    if "Voros_Rokak"==i.hazai or "Voros_Rokak"==i.vendeg:
        if nap_min>i.nap:
            nap_min=i.nap
        elif nap_max<i.nap:
            nap_max=i.nap
print(f"Először az év {nap_min}-dik napján, utoljára pedig az év {nap_max}-dik napján játszik.")

print("4. feladat")
ki=open("egri.txt", "w", encoding="utf-8")
for i in lista:
    if "Egri_Csillagok"==i.hazai or "Egri_Csillagok"==i.vendeg:
        ki.write(f"{i.hazai} {i.vendeg} {i.nap} \n")
ki.close()

print("5. feladat")
db=0
jegyar=0
for i in lista:
    if "Voros_Rokak"==i.hazai or "Voros_Rokak"==i.vendeg:
        jegyar+=i.jegy
    if "Computerbonto"==i.hazai or "Computerbonto"==i.vendeg:
        jegyar+=i.jegy
    if "Bohocok"==i.hazai or "Bohocok"==i.vendeg:
        jegyar+=i.jegy
print(f"Kedvenc csapatainak mérkőzéseire a jegyár összesen: {jegyar}Ft.")

print("6. feladat")
csapatnev=input("Kérlek adj meg egy csapatnevet: ")
db=0
napok=[]
for i in lista:
    if csapatnev.lower()==i.hazai.lower() or csapatnev==i.vendeg.lower():
        napok.append(i.nap)
        db+=1
    if csapatnev.upper()==i.hazai.upper() or csapatnev==i.vendeg.upper():
        napok.append(i.nap)
        db+=1
print(f"Játszik ebben az idényben, az év következő napjain: {napok}" if db>0 else f"Nem szerepel a mezőnyben.")