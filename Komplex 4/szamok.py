szam=1
prim=[]
nemprim=[]
szamok=[]

def prim_e(x):
            db=0
            for i in range(1, x+1):
                if x%i==0:
                    db += 1
            if db == 2:
                return True
            else:
                return False

while szam!=0:
    szam=int(input("A szám: "))
    if szam==0:
        break
    szamok.append(szam)

for i in szamok:
    if prim_e(i)==True:
        prim.append(i)
    else:
        nemprim.append(i)

print(f"Prímszámok: {prim}")
print(f"Nem prímszámok: {nemprim}")
print(f"Az összes szám átlaga: {sum(szamok)/len(szamok):.2f}")

if len(prim)>0:
    print(f"A legnagyobb prímszám: {max(prim)}")