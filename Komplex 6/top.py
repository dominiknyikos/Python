class Toplista():
    def __init__(self,s):
        sor=s.split(";")
        self.het=int(sor[0])
        self.helyezes=int(sor[1])
        self.zeneszam=sor[2]
        self.eloado=sor[3]
        self.nyelv=int(sor[4])
lista=[]
with open("toplista.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Toplista(i.strip()))
f.close()

print(f"Összesen {len(lista)}db szám van a nyilvántartásban.")

het=1
for i in lista:
    if i.helyezes==1:
        print(f"{i.het} hét nyertese: {i.eloado} - {i.zeneszam}")
        het+=1

db=0
for i in lista:
    if i.helyezes<=20 and i.nyelv==1:
        db+=1
print(f"Az első 20 hely egyikében {db} magyar előadó volt.")

eloado=input("Add meg egy előadó nevét: ")
cimek=0
pontszam=0
for i in lista:
    if (eloado).lower()==(i.eloado).lower():
        print(f"{i.het}.hét - {i.helyezes} helyezés - {i.zeneszam} című zenével.")
        cimek+=1
        pontszam+=(41-i.helyezes)*10
    elif (eloado).upper()==(i.eloado).upper():
        print(f"{i.het}.hét - {i.helyezes} helyezés - {i.zeneszam} című zenével.")
        cimek+=1
        pontszam+=(41-i.helyezes)*10
print(f"Az általad választott előadó összesen {pontszam} pontot ért el.")
if cimek==0:
    print(f"Nincs ilyen előadó!")

helyezesek=[]
for i in lista:
    if i.eloado=="AVICII":
        helyezesek.append(i.helyezes)
print(f"AVICII előadó átlagosan {sum(helyezesek)/len(helyezesek):.0f}. helyezést ért el!")

sorszam=int(input("Adj meg egy számot 1 és 7 között: "))
ki=open(f"{sorszam}.txt", "w", encoding="utf-8")
for i in lista:
    if sorszam==i.het:
        ki.write(f"{i.eloado} - {i.zeneszam} - {(41-i.helyezes)*10}pont \n")
ki.close()