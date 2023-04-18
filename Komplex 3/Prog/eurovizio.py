class Eurovizio():
    def __init__(self,s):
        sor=s.split(";")
        self.ev=int(sor[0])
        self.orszag=sor[1]
        self.eloado=sor[2]
        self.cim=sor[3]
        self.helyezes=int(sor[4])
lista=[]
with open("eurovizio.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Eurovizio(i.strip()))
f.close()
print(f"Összesen {len(lista)} zeneszám van")

for i in lista:
    if "dream" in i.cim.lower():
        print(f"{i.eloado}: {i.cim}")
    elif "dream" in i.cim.upper():
        print(f"{i.eloado}: {i.cim}")

orszag=input("Írj be egy országot: ")
db=0
for i in lista:
    if orszag==i.orszag:
        db+=1
print(f"Összesen {db} alkalommal szerepelt az adott ország.")

def pontszam(helyezes):
    return 101-helyezes
lista_masodik=[]
for i in lista:
    if i.orszag=="Magyarország":
        lista_masodik.append(pontszam(i.helyezes))
print(f"A magyarországi versenyzők átlagos pontszáma: {sum(lista_masodik)/len(lista_masodik):.2f}")