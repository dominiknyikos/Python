"""
for i in range(1,11):
    print(i, end="; ")
"""

"""
i=1
while i<11:
    print(i, end=",")
    i+=2
"""

"""
for i in range(1,201,2):
    print(i, end="; ")
"""

"""
for i in range(3,151,3):
    print(i, end="; ")
"""

"""
i=3
while i<151:
    if i%3==0:
        print(i, end="; ")
    i+=1
"""

"""
for i in range(10,100,5):
    print(i, end="; ")
"""

"""
for i in range(1,11):
    print(2**i, end="; ")
"""

"""
import math
for i in range(1,11):
    i=math.pow(2,i)
print(int(math.pow(2,1)))
"""

"""
for i in range(1,6):
    for j in range(1,6):
        if i==j or i+j==6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""

"""
szam=int(input("100-nál kisebb számot adj meg: "))
prim=True

for oszto in range(2,szam):
    if szam%oszto==0:
        prim=False
print("Prím" if prim==True else "Összetett")
"""

"""
szam=int(input("100-nál kisebb számot adj meg: "))
osszeg=0

for oszto in range(1,szam):
    if szam%oszto==0:
        osszeg+=oszto
print("Tökéletes szám" if osszeg==szam else "Nem tökéletes szám")
"""