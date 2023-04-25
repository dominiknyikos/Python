import random
n=int(input("Mennyi eredmény legyen generálva: "))
eredmenyek=[]
felettiek=[]

print("A generált számok:")
for i in range(n):
    eredmenyek.append(random.randint(0,100))
for i in eredmenyek:
    print(i)
print(f"A százalékok átlaga: {sum(eredmenyek)/len(eredmenyek):.2f}")

def hatvan(szam):
    if szam>60:
        return True
for i in eredmenyek:
    if hatvan(i):
        felettiek.append(i)
print(f"60% feletti százalékértékek: {felettiek}")

db=0
for i in felettiek:
    if i==100:
        db+=1
if db>0:
    print(f"100%-os százalékértékek: {db}")
else:
    print("Nem volt 100%-os eredmény!")