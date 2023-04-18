import random
lista=[]
szam=int(input("Kérlek adj meg egy számot: "))
while szam!=0:
    lista.append(szam)
    szam=int(input("Kérlek adj meg egy számot: "))

def azonos_e(szam):
	if szam%11==0:
		return True
db=0
for i in lista:
    if azonos_e(i):
        db+=1
print(f"Azonosjegyek száma: {db}")

osszeg=0
darab=0
for i in lista:
      if i%5==0:
            osszeg+=szam
            db+=1
print(f"{osszeg/db}")

for i in lista:
      if i>60 and i<70:
            print(i)
            break
      
for i in lista:
      if i==50:
            print("Van")