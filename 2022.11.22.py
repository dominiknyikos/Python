"""
import random
lista=[] #Üres lista
for i in range(10): #10 számot generál
    lista.append(random.randint(1,1000))
print(lista)
"""

"""
lista.insert(4,50) #bővítés az ötödik helyre 50-est
print(len(lista)) #len hogya listaba mennyi elem van
print(lista.index(50)) #hanyadik helyen található az 50
print(lista.count(50)) #hány db 50 szám van
print(lista.remove(50)) #kitörli az 50-et
"""

"""
print(lista[::-1]) #Forditrott sorrendbe kiiras
print(lista[1:8:2]) #Másodikat kiírja 1-8 elemig
print(lista[7:3:-1]) #7-től 3-ig
print(sum(lista)) #Összeadja a listát
print(sum(lista)/len(lista)) #A lista elemeinek átlaga
"""

"""
db=0

for i in lista:
    if i>9 and i<100:
        db+=1
print(db)
print(len([x for x in lista if x>9 and x<100]))
print([x**2 for x in lista if x>0 and x<10])
print(sum([x for x in lista if x%3==0]))
print(len([x for x in lista if x%10==0]))
print(max([x for x in lista if x%5==0]))
print(len([x for x in lista if x>500 and x<1000]))
print(sum([x for x in lista if x>-10 and x<10]))
print(sorted([x for x in lista if x>9 and x<100])) #Növekvő sorrend
print(sorted([x for x in lista if x>9 and x<100])[::-1]) #Csökkenő sorrend
"""

mondat=input("Kérlek írj be egy mondatot: ")
szo=input("Szó: ")

"""
print(mondat.count(" ")+1)
print(len(mondat))
mgh=['a', 'á', 'e', 'é', 'o', 'ó']
db=0
for i in mondat:
    if i in mgh:
        db+=1
print(db)

mennyiszer=int(input("Hányszor: "))
print((mondat+" ")*mennyiszer)
"""

ind=mondat.index(" ")
elso=(mondat[:ind+1]+szo)
masodik=(mondat[ind:])

print(elso + masodik)