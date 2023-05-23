import random
n=int(input("Mennyi generálás legyen: "))
szamok=[]
lista=[]

for i in range(n):
    szamok.append(random.randint(1,50))
    lista.append(f"{i}:{szamok[i]}")
    print(szamok[i])

print("Zivataros napok: ", end="")
for i in range(n):
    if i%10==0:
        print(f"{i}:{szamok[i]}", end=" ")
print()

print("Felhős napok: ", end="")
for i in range(n):
    if i%2==0 and i%10!=0:
        print(f"{i}:{szamok[i]}", end=" ")
print()
#A feladatsor a napokat kéri vizsgálni, nem pedig a napi időjárást!

print(f"A generálások összege: {sum(szamok)}")
print(f"A generálások átlaga: {round(sum(szamok)/len(szamok))}")