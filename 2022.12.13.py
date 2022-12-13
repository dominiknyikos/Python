import random
lista=[]
db=0

for i in range(10):
    lista.append(random.randint(1,100))
print(lista)
osszeg=0
for i in lista:
    if i>50:
        osszeg+=1
print(f"A lista elemeinek összege: {osszeg}, darab: {db}")
print(sum([x for x in lista if x>50]))

n=len(lista)
ker=5
i=0

while i<n and lista[i]!=50:
    i=i+1
print(f"Van benne 50-es, helye {i}" if i<n else "Nincs benne")

paros=[]
paratlan=[]

for i in lista:
    if i%2==0:
        paros.append(i)
    else:
        paratlan.append(i)
print(paros)
print(paratlan)

max=lista[0]
min=lista[0]
maxi=0
mini=0

for i in range(len(lista)):
    if lista[i]>max:
        max=lista[i]
        maxi=i
    elif lista[i]<min:
        min=lista[i]
        mini=i
print(f"Legnagyobb elem: {max}, helye: {maxi}")
print(f"Legkisebb elem: {min}, helye: {mini}")

for i in range(0,len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i]>lista[j]: #Ha megfordítom a relációs jelet, akkor csökkenő sorrendbe írja ki.
            csere=lista[i]
            lista[i]=lista[j]
            lista[j]=csere
print(lista)