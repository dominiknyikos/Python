class Auto:
    def __init__(self, sor):
        sor=sor.split(";")
        self.rendszam = sor[0]
        self.marka = sor[1]
        self.szin = sor[2]
        self.gyev = int(sor[3])
lista=[]
with open("auto.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Auto(i.strip()))
f.close()

print(f"A kereskedésben {len(lista)}db autó van jelenleg.")

for i in lista:
    betu=i.rendszam[0]
    szam=i.rendszam[3]
    if szam==i.rendszam[4] and szam==i.rendszam[5]:
        print(f"{i.rendszam} {i.marka}")
    elif betu==i.rendszam[1] and betu==i.rendszam[2]:
        print(f"{i.rendszam} {i.marka}")

kereses=input("Adja meg a keresni kívánt márkanevet! ")
db=0
eletkor=[]
for i in lista:
    if (kereses).upper()==(i.marka).upper():
        db+=1
        eletkor.append(2023-i.gyev)
    elif (kereses).lower()==(i.marka).lower():
        db+=1
        eletkor.append(2023-i.gyev)
print(f"A kereskedésben {db} db {(kereses).upper()} van.")

if db>0:
    print(f"Ezek átlag életkora {sum(eletkor)/db} év.")

legregebbi=2023
rendszam=""
marka=""
szin=""
for i in lista:
    if i.gyev<legregebbi:
        legregebbi=i.gyev
        rendszam=i.rendszam
        marka=i.marka
        szin=i.szin
print(f"A legrégebbi autó: {rendszam} {marka} {szin} {legregebbi}")

"""
ki=open("ki.txt", "w", encoding="utf-8")
for i in lista:
    ki.write(i.marka +"\n")
ki.close()
"""