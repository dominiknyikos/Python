class Forditas():
    def __init__(self,s):
        sor=s.split(",")
        self.nev=sor[0]
        self.elerhetoseg=sor[1]
        self.forrasnyelv=sor[2]
        self.celnyelv=sor[3]
        self.egysegar=int(sor[4])
lista=[]
with open("forditok.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Forditas(i.strip()))
f.close()

feladat2=len(lista)
print(f"Fordítók száma: {feladat2}")

for i in lista:
    if i.elerhetoseg=="i" and i.forrasnyelv=="angol" and i.celnyelv=="magyar":
        print(f"{i.nev} - {i.egysegar}")

db=0
osszeg=0
for i in lista:
    if i.celnyelv!="magyar" or i.celnyelv!="angol":
        osszeg+=i.egysegar
        db+=1
feladat3=round(osszeg/db)
print(f"Átlagos fordítási összegük: {feladat3}")

darab=0
nyelv=input("Adj meg egy nyelvet: ")
for i in lista:
    if nyelv==i.celnyelv and i.elerhetoseg=="i":
        print(f"{i.nev} - {i.forrasnyelv} - {i.egysegar}")
        darab+=1
if darab==0:
    print("A megadott nyelvre nincs fordítási szolgáltatás.")

def atvaltas(lista,arfolyam=375):
    euro=i.egysegar/arfolyam
    return euro
atvaltas(lista)

nyelv=input("Adj meg egy nyelvet: ")
ki=open(f"{nyelv}.txt", "w", encoding="utf-8")
for i in lista:
    if nyelv==i.forrasnyelv:
        ki.write(f"{i.nev} - {i.celnyelv} - {i.egysegar} \n")