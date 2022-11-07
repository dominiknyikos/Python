"""
a=int(input ("Kérem az a értékét"))
m=int(input ("Kérem az m értékét"))

print(f"Téglatest térfogata, amelynek a az oldala {a} és m a magassága {m}, térfogata V= {a**2*m} és felszíne A={4*a*m+2*a**2}")
"""


"""
szam=int(input ("Kérek egy egész számot"))

if szam>0:
    print(f"A szám pozitív")
elif szam==0:
    print(f"A szám nulla")
else:
    print(f"A szám negatív")
"""


"""
x=int(input ("Kérem az x értékét"))
y=int(input ("Kérem az y értékét"))

if x>0 and y>0:
    print(f"Első negyedben van")
elif x>0 and y<0:
    print(f"Második negyedben van")
elif x<0 and y<0:
    print(f"Harmadik negyedben van")
elif x<0 and y<0:
    print(f"Negyedik negyedben van")
elif x==0 and y!=0:
    print(f"Az x tengelyen helyezkedik el")
elif x!=0 and y==0:
    print(f"Az y tengelyen helyezkedik el")
else:
    print(f"Az origóban helyezkedik el")
"""


"""
#Páros szám-e?
c=int(input ("Kérek egy egész számot"))

if c%2==0:
    print(f"A szám páros")
else:
    print(f"A szám páratlan")
"""


"""
#n osztható-e m-mel?
n=int(input ("Kérem az n értékét"))
m=int(input ("Kérem az m értékét"))

if m!=0:
    if n%m==0
        print(f"m osztója n-nek")
    else:
        print(f"m nem osztója n-nek")
else:
    print(f"Nem adhatsz meg 0-át")
"""


"""
#3. feladat
a=int(input ("Kérem az a értékét"))
b=int(input ("Kérem az b értékét"))
n=int(input ("Kérem az n értékét"))

if n>a and n<b:
    print(f"Beletartozik az intervallumba")
elif n<a and n>b:
    print(f"Nem tartozik bele az intervallumba")
else:
    print(f"Szöveg")
"""


"""
#4. feladat
jegy=int(input(f"Kérek egy egész számot 1-től 5-ig"))

if jegy==1:
    print(f"Elégtelen")
elif jegy==2:
    print(f"Elégséges")
elif jegy==3:
    print(f"Közepes")
elif jegy==4:
    print(f"Jó")
elif jegy==5:
    print(f"Jeles")
else:
    print(f"1-től 5-ig fogadok be számot.")
"""


"""
#5. feladat
nap=input(f"Kérlek adj meg egy napot")

if nap=="Hétfő":
    print(f"Első nap")
elif nap=="Kedd":
    print(f"Második nap")
elif nap=="Szerda":
    print(f"Harmadik nap")
elif nap=="Csütörtök":
    print(f"Negyedik nap")
elif nap=="Péntek":
    print(f"Ötödik nap")
elif nap=="Szombat":
    print(f"Hatodik nap")
elif nap=="Vasárnap":
    print(f"Hetedik nap")
else:
    print(f"Nem letéző napot adtál meg.")
"""


"""
#6. feladat
a=int(input(f"Kérlek add meg az egyik befogó értékét"))
b=int(input(f"Kérlek add meg a másik befogó értékét"))

if a+b==90:
    print(f"A háromszög derékszögű")
else:
    print(f"A háromszög nem derékszögű")
"""


"""
#7. feladat
a=int(input(f"Kérlek add meg az a értékét"))
b=int(input(f"Kérlek add meg a b értékét"))
c=int(input(f"Kérlek add meg a c értékét"))

if a+b>c and b+c>a:
    print(f"A háromszög szerkeszthető")
else:
    print(f"A háromszög nem szerkeszthető")
"""


"""
#8. feladat
a=int(input(f"Kérlek add meg az a értékét"))
b=int(input(f"Kérlek add meg a b értékét"))
c=int(input(f"Kérlek add meg a c értékét"))
D=b**2-4*a*c

if D>0:
    print(f"Kettő gyöke van")
elif D==0:
    print(f"Egy gyöke van")
else:
    print(f"Nincs gyöke")
"""


"""
#9. feladat
evszam=int(input(f"Kérlek adj meg egy évszámot"))

if evszam % 4==0 or evszam % 400==0:
    print(f"Szökőév")
elif evszam % 100!=0:
    print(f"Nem szökőév")
else:
    print(f"Nem szökőév")
"""


"""
#10. feladat
n=int(input(f"Kérlek adj meg egy számot"))

if n<10 and n>-10:
    print(f"egyszámjegyű")
elif n<100 and n>-100:
    print(f"kétszámjegyű")
elif n<1000 and n>-1000:
    print(f"háromszámjegyű")
elif n<10000 and n>-10000:
    print(f"négyszámjegyű")
elif n<100000 and n>-100000:
    print(f"ötszámjegyű")
elif n<1000000 and n>-1000000:
    print(f"hatszámjegyű")
elif n<10000000 and n>-10000000:
    print(f"hétszámjegyű")
elif n<100000000 and n>-100000000:
    print(f"nyolcszámjegyű")
else:
    print(f"több mint kilcenszámjegyű")
"""