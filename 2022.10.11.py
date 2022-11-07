"""
a=int(input(f"Kérlek adj meg egy egész számot"))

if a%3==0 and a%5==0:
    print(f"fizzbuzz")
elif a%3==0:
    print(f"fizz")
elif a%5==0:
    print(f"buzz")
else:
    print(f"{a} nem osztható 3-mal és 5-tel!")
"""


"""
import random
gondolt_szam=random.randint(1,100)
tipp=int(input("Szám:"))
lepes=0
kitaltad=False

while kitaltad==False:
    if tipp==gondolt_szam:
        lepes+=1
        print(f"{lepes}-ből találtad ki")
        kitaltad=True
    elif tipp>gondolt_szam:
        print("Adj kisebb számot")
        lepes+=1
        tipp=int(input())
    elif tipp<gondolt_szam:
        print("Adj nagyobb számot")
        lepes+=1
        tipp=int(input())
    else:
        print(f"Rossz")
"""


"""
# 100-1-ig kérem a páratlan számokat
i=100 #kezdőérték a ciklusváltozónak

while 101>i and i>=1:
    if i%2==1:
        print(i, end=";")
    i-=1
"""


"""
n=int(input("Kérem a számot"))
i=1
fakt=1

while i<=n:
    fakt=fakt*i
    i+=1
print(fakt)
"""


"""
import random

szam=int(input(f"Kérlekk add meg a számot, amire gondoltál (1-től 100-ig)"))
tipp=random.randint(1,100)
lepes=1

if szam<1 or szam>100:
    print(f"Kérlek 1-től 100-ig adj meg számot.")
print ("A gép erre gondolt:", tipp)

while tipp!=szam:
    if tipp>szam:
        tipp-=1
        tipp=random.randint(1, tipp)
        lepes+=1
    else:
        lepes+=1
        tipp=random.randint(tipp, 100)
    print ("A gép erre gondolt:", tipp)
print ("A gép erre gondolt:", tipp, "és helyes volt,", lepes, "lépésből találta ki.")
"""