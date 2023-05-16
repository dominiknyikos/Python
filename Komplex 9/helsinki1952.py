class Sport():
    def __init__(self,s):
        sor=s.split(" ")
        self.helyezes=int(sor[0])
        self.sportolok=int(sor[1])
        self.sportag=sor[2]
        self.versenyszam=sor[3]
lista=[]
with open("helsinki.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Sport(i.strip()))
f.close()

print("3. feladat")
print(f"Pontszerző helyezések száma: {len(lista)}")

print("4. feladat")
arany=0
ezust=0
bronz=0
for i in lista:
    if i.helyezes==1:
        arany+=1
    elif i.helyezes==2:
        ezust+=1
    elif i.helyezes==3:
        bronz+=1
print(f"Arany: {arany}")
print(f"Ezüst: {ezust}")
print(f"Bronz: {bronz}")
print(f"Összesen: {arany+ezust+bronz}")

print("5. feladat")
pontok=0
for i in lista:
    if i.helyezes==1:
        pontok+=7
    elif i.helyezes==2:
        pontok+=5
    elif i.helyezes==3:
        pontok+=4
    elif i.helyezes==4:
        pontok+=3
    elif i.helyezes==5:
        pontok+=2
    elif i.helyezes==6:
        pontok+=1
print(f"Olimpiai pontok száma: {pontok}")

print("6. feladat")
uszas=0
torna=0

for i in lista:
    if i.sportag=="uszas":
        uszas+=1
    elif i.sportag=="torna":
        torna+=1

if uszas<torna:
    print("Torna sportágban szereztek több érmet")
elif uszas>torna:
    print("Úszás sportágban szereztek több érmet")
else:
    print("Egyenlő volt az érmek száma")

ki=open("helsinki2.txt", "w", encoding="utf-8")
for i in lista:
    if i.helyezes==1:
        ki.write(f"{i.helyezes} {i.sportolok} 7 {i.sportag} {i.versenyszam}\n")
    elif i.helyezes==2:
        ki.write(f"{i.helyezes} {i.sportolok} 5 {i.sportag} {i.versenyszam}\n")
    elif i.helyezes==3:
        ki.write(f"{i.helyezes} {i.sportolok} 4 {i.sportag} {i.versenyszam}\n")
    elif i.helyezes==4:
        ki.write(f"{i.helyezes} {i.sportolok} 3 {i.sportag} {i.versenyszam}\n")
    elif i.helyezes==5:
        ki.write(f"{i.helyezes} {i.sportolok} 2 {i.sportag} {i.versenyszam}\n")
    elif i.helyezes==6:
        ki.write(f"{i.helyezes} {i.sportolok} 1 {i.sportag} {i.versenyszam}\n")
ki.close()

print("8. feladat")
db=0
helyezes=0
sportag=""
versenyszam=""
for i in lista:
    if i.sportolok>db:
        db=i.sportolok
        helyezes=i.helyezes
        sportag=i.sportag
        versenyszam=i.versenyszam
print(f"Helyezés: {helyezes}")
print(f"Sportág: {sportag}")
print(f"Versenyszám: {versenyszam}")
print(f"Sportolók száma: {db}")