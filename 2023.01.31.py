"""
#Szám osztóinak a meghatározása eljárással.
def osztoi(szam):
    oszto=1
    while oszto<=szam:
        if szam%oszto==0:
            print(oszto)
        oszto+=1
osztoi(50)
osztoi(100)
"""


"""
#Szám osztóinak a meghatározása függvénnyel.
def osztok(szam):
    l=[]
    oszto=1
    while oszto<=szam:
        if szam%oszto==0:
            l.append(oszto)
        oszto+=1
    return l #Visszaadott érték, egy lista.
osztok(50) #Függvény meghívása.
print(osztok(50))
"""


"""
#Két szám összege.
def osszeg(a,b):
    return a+b
print(osszeg(5,7))
"""


"""
#1. feladat: Adott számig eljárással írd ki a páros számokat.
def paros(szam):
    paros=1
    while paros<=szam:
        if paros%2==0:
            print(paros)
        paros+=1
print(paros(20))
"""


"""
#2. feladat: Adott számig határozd meg a páros számok számát függvénnyel.
l=[]
def paros(szam):
    paros=1
    while paros<=szam:
        if paros%2==0:
            l.append(paros)
        paros+=1
    return l
print(paros(20))
print(len(l))
"""


"""
#3. feladat
def leghosszabb_szo(s): #Ma nem veszek almát.
    if s=="":
        return "Hiba!"
    else:
        l=s.split() #l=["Ma", "nem", "veszek", "almát."]
        #maximum kiválasztás tétele
        max=len(l[0]) #2-vel jön vissza.
        maxi=0
        for i in range(len(l)): #Indexes
            if max<len(l[i]):
                max=len(l[i])
                maxi=i
        return l[maxi]
print(leghosszabb_szo(input("Kérek egy mondatot: ")))
"""


"""
#4. feladat
def gyenge_jelszavak(lista):
    gyenge=[]
    for i in lista:
        if len(i)<5:
            gyenge.append(i)
        elif i.isalpha():
            gyenge.append(i)
        elif "jelszo" in i or "123" in i:
            gyenge.append(i)
        return gyenge
lista=["fgb", "jelszo456", "123fkj15", "Lfds7889v"]
print(gyenge_jelszavak(lista))
"""


"""
#5. feladat
def egyedi_szavak_szama(s): #Ma nem eszünk káposztát, mert a kecske megette a káposztát.
    s=s.lower() #Egész szöveg kisbetüssé alakítása.
    s=s.replace(".","").replace(",","")
    l=s.split()
    halmaz=set(l)
    return len(halmaz)
print((egyedi_szavak_szama("Ma nem eszünk káposztát, mert a kecske megette a káposztát.")))
"""

#6. feladat
def felváltva(s):
    l=s.split()
    if len(l)<2:
        return "Hiba!"
    else:
        for i in range(len(l)):
            if i%2==0:
                l[i]=l[i].upper()
            else:
                l[i]=l[i].lower()
    uj=(" ").join(l)
    return uj
print(felváltva("Ma nem eszünk káposztát, mert a kecske megette a káposztát."))