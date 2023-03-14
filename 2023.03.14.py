"""
#A feladat
f=open("kutya.txt", "r", encoding="utf-8")
lista=[]
for i in f:
    lista.append(i.strip())
print(lista)

#1. Hány sorból áll a txt?
print(len(lista))

#2. Melyik a leghosszabb név?
max_hossz=len(lista[0])
maxi=0
for i in range(len(lista)):
    if len(lista[i])>max_hossz:
        max_hossz=len(lista[i])
        maxi=i
print(lista[maxi])

#3. írjunk függvényt, hogy a bekért név szerepel-e a nevek között.
def benne(lista,nev):
    if nev in lista:
        return True
nev=input("Kérek egy nevet: ")
if benne(lista,nev)==True:
    print("Szerepel benne.")
else:
    print("Nem szerepel benne.")

#4. írjuk ki "nevek_i.txt" fájlba az i-re végződő neveket.
ki=open("nevek_i.txt", "w", encoding="utf-8")
for elem in lista:
    if elem.endswith("i"):
        ki.write(elem)
ki.close()

#5. Hány olyan név van, amely 5 karakter hosszú függvénnyel?
db=0
for i in lista:
    if len(i)==5:
        db+=1
print(db)
"""

"""
#B feladat
class Verseny():
    def __init__(self,s):
        sor=s.split("\t")
        self.nev=sor[0]
        self.szuletesi_datum=sor[1]
        self.nemzetiseg=sor[2]
        self.rajtszam=int(sor[3])
lista=[]
with open("versenyzok.txt", "r", encoding="utf-8") as f:
    f.readline()
    for i in f:
        lista.append(Verseny(i.strip()))

#1. Hány versenyző van?
print(len(lista))

#2. Hány német versenyző van?
db=0
for i in lista:
    if i.nemzetiseg=="német":
        db+=1
print(db)

#3. Milyen nemzetiségű versenyzők vannak a fájlban?
nemzet=[]
for i in lista:
    if i.nemzetiseg in nemzet:
        continue
    else:
        nemzet.append(i.nemzetiseg)
print(nemzet)

nemzetek=[]
for i in lista:
    nemzetek.append(i.nemzetiseg)
print(set(nemzetek))
"""