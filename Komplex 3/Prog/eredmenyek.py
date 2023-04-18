import random
n=int(input("Mennyi eredmény legyen generálva: "))

db=0
eredmenyek=[]
eredmeny=0
feletti_eredmenyek=[]
hibatlan=0
print("A generált számok: ")
while n>db:
    db+=1
    eredmeny=random.randint(0,100)
    if eredmeny==100:
        hibatlan+=1
        feletti_eredmenyek.append(eredmeny)
    elif eredmeny>60:
        feletti_eredmenyek.append(eredmeny)
    eredmenyek.append(eredmeny)
    print(eredmeny)
print(f"A százalékok átlaga: {sum(eredmenyek)/len(eredmenyek):.2f}")
print(f"60% feletti százalékértékek: {feletti_eredmenyek}")
print(f"100%-os százalékértékek: {hibatlan}")