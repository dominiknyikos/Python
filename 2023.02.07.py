#1. feladat
def csillag(s):
    print(len(s)*"*")
csillag("ablak")


#2. feladat
def szamok(szam):
    if szam<=0:
        print("Hiba!")
    else:
        uj=""
        for i in range(szam):
            if i%3==0:
                uj+="+"
            else:
                uj+="-"
        print(uj)
szamok(20)


#3. feladat
def mondat(s):
    print(s[::-1])
mondat("Ma süt a nap.")


#4. feladat
def szokoz(s):
    s=s.replace(" ", "")
    print(s)
szokoz("Ma süt a nap.")


#5. feladat
lista=["Én", "elmentem", "a", "vásárba", "fél", "pénzen."]
print(len(lista))
print(len(min(lista)))

tartalmaz=False
for i in lista:
    if "." in i:
        tartalmaz=True
print("Van benne." if tartalmaz==True else "Nincs benne.")

print(lista.count("a"))
print(lista.count("az"))
print(lista.index("fél"))

van=False
for i in lista:
    if i.isupper():
        van=True
print("Van benne." if van==True else "Nincs benne.")


#6.1 feladat
def masol(s1, s2):
    index=len(s2)
    uj=s2+s1[index:]
    return uj
print(masol("alma", "fa"))


#6.4 feladat
def karakter(kar, s):
    index=s.find(kar)
    if index==-1:
        return "Nincs benne ilyen karakter."
    else:
        return index+1
print(karakter("a", "alma"))


"""
#Van valami hiba a megoldásban.
#6.5. feladat
def betuk(s):
    uj=""
    for i in s:
        if i.isupper():
            uj+=i.lower
        else:
            uj+=i.upper
    return uj
print(betuk("euROhuf"))
"""

#6.6 feladat
def fesul(s1, s2):
    uj=""
    hossz1=len(s1)
    hossz2=len(s2)
    if hossz1==hossz2:
        for index in range(len(s1)):
            uj+=s1[index]+s2[index]
        return uj
    elif hossz2>hossz1:
        for index in range(len(s1)):
            uj+=s1[index]+s2[index]
        uj+=s2[hossz1:]
        return uj
    else:
        for index in range(len(s2)):
            uj+=s1[index]+s2[index]
        uj+=s1[hossz2:]
        return uj
print(fesul("alma", "123"))