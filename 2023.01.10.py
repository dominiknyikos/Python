import random
"""
#1. feladat
fuvar=[]
for i in range(10):
    fuvar.append(random.randint(1,10))
print(fuvar)
print(f"Összesen kapott pénze: {sum(fuvar)}")
print(f"Átlagkeresete: {sum(fuvar)/len(fuvar)} picula")

van=False
for i in fuvar:
    if i==5:
        van=True
if van:
    print(f"Volt 5 piculás fuvarja")
else:
    print(f"Nem volt 5 piculás fuvarja")
for i in range(len(fuvar)):
    if fuvar[i]==5:
        print(f"{i+1}. fuvar volt 5 piculás fuvar")

max=fuvar[0]
maxi=0
for i in range(len(fuvar)):
    if fuvar[i]>max:
        max=fuvar[i]
        maxi=i 
print(f"A legtöbb piculát kapta: {maxi+1}. fuvarral")      
"""


"""
#2. feladat
liba=[]
for i in range(5):
    liba.append(random.randint(1,7))
print(liba)
farkas=[]
roka=[]
for i in liba:
    if i>3:
        farkas.append(i)
    else:
        roka.append(i)
print(farkas)
print(roka)
print(f"{sum(roka)} kg libát ehet meg a róka")
print(f"{sum(roka)/len(roka)} kg az átlag")

igen=False
for i in liba:
    if i>=3:
        igen=True
if igen:
    print("Előfordult")
else:
    print("Nem fordult elő")

van=False
j=1
for i in range(len(liba)-1):
    for j in range(len(liba)):
        if liba[i]>liba[j]:
            van=True
if van:
    print("Kisebb libát hozott")
else:
    print("Nem fordult elő kisebb")
for i in range(len(liba)):
    if liba[i]>=3:
        print(i+1)
        break
print(f"{min(farkas)} legkisebb tömegű liba a farkasnál")
"""


"""
#3. feladat
pincer=[3, 8, 10, 19.35, -6, 5.1, 9, 20]
volt=False
for i in pincer:
    if i<0:
        volt=True
if volt:
    print("Vásárolt")
else:
    print("neki fizettek")
print(f"{sum(pincer)} Ft")

db=0
penny=[]
for i in pincer:
    if i%1!=0:
        db+=1
        penny.append(i)
print(db)

egesz=int(sum(penny))
print(f"penny összesen:{(sum(penny)-egesz)*100}")
alkalom=0
for i in pincer:
    if i>=5:
        alkalom+=1
print(f"{alkalom}-mal alkalommal kapott legalább 5 fontot")

max=pincer[0]
for i in range(len(pincer)):
    if max<pincer[i]:
        max=pincer[i]

print(f"legnagyobb összeg:{max}")
valto=8.23
for i in pincer:
    valto+=i
print(f"összesen:{valto}")
print(f"{pincer.index(9)+1}. vendég fizetett 9 fontot")

for i in range(len(pincer)):
    if pincer[i]>10:
        print(i)
        break

index=0
for i in range(len(pincer)):
    if pincer[i]>10:
        index=i
print(f"utolsó: {index}")

ot=False
for i in pincer:
    if i%5==0:
        ot=True
if ot:
    print("Volt ilyen vendég")
else:
    print("Nem volt")

fizet=0
for i in pincer:
    if i>0:
        fizet+=1
print(f"{fizet*0.5} bevételt kapott")
"""


"""
#4. feladat
mondat=["Én", "elmentem", "a",
"vásárba", "fél", "pénzen."]
print(f"len(mondat) szóból áll")
betu=[]
for i in mondat:
    betu.append(len(i))
print(f"legrövidebb szó:{min(betu)}-ből áll")
irasjel=["!","?","."]
iras=False
for i in mondat:
    for j in i:
        if j in irasjel:
            iras=True
if iras:
    print("van írásjeles")
else:
    print("nincs")

nevelo=0
for i in mondat:
    if i=="a" or i=="az":
        nevelo+=1
print(f"{nevelo} névelő van a mondatban")
print(mondat.index("fél")+1)
"""