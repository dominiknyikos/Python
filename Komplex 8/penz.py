#1. Feladat
import random
arfolyam=random.randint(380,450)
forint=int(input("Átváltandó összeg: "))

print(f"{forint/arfolyam:.0f} eurót kaptál.")

if arfolyam>=380 and arfolyam<=390:
    print("Érdemes")
else:
    print("Nem érdemes")

#2. Feladat
kezdo=int(input("Kezdő pénz: "))
porgetes=int(input("Pörgetések száma: "))
ertek=0
lista=[]
nyeremeny=0

for i in range(porgetes):
    ertek=random.randint(0,36)
    lista.append(ertek)
    if ertek==0:
        nyeremeny=0
    elif ertek==36:
        nyeremeny+=500000
    elif ertek%2==0:
        nyeremeny+=2000
    elif ertek%2!=0:
        nyeremeny-=2000

print(f"A nyeremény összege: {nyeremeny}")
print(f"A pörgetések átlaga: {sum(lista)/len(lista):.0f}")
print(f"A legnagyobb kipörgetett szám: {max(lista)}")

if 20 not in lista:
    print("Nem volt 20 pörgetve.")

def egyszer(lista):
    halmaz=set(lista)
    return halmaz
egyszer(lista)
print("A pörgetett számok: {lista}")