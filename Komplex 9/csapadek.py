import random
szam=0
lista=[]
for i in range(10):
    szam=random.randint(0,30)
    lista.append(szam)
    print(szam)
print(f"Az összes csapadék: {sum(lista)}")
print(f"Az átlagos csapadék: {sum(lista)/len(lista)}")

paros=[]
paratlan=[]
def paros(szam):
    if szam%2==0:
        return True
    else:
        return False
for i in lista:
    if paros(i)==True:
        print(i, end=" ")
print("\n ------------------")
for i in lista:
    if paros(i)==False:
        print(i, end=" ")