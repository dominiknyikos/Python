"""
a=5
print(a)
print(type(a))

b=2.963
print(type(b))

s="alma"
print(type(s))

l=True
print(type(l))

print("A két szám összege", a+b)
c=a-b
print("A {0} szám és {1} szám különbsége= {2:.1f}" .format(a,b,c))
#f-stringes kiíratása
print(f"A {a} és {b} szám szorzata ={a*b:.2f}")
print(f"A {a} és {b} szám hányadosa ={a/b:.3f}")
print(f"A {a} és {b} szám hányadosa ={a//b:.3f}")
print(f"A {a} és {b} szám hatváya ={a**b:.3f}")
"""

#1. Gömb fekszínének és térfogatának kiszámítása
from cgi import print_arguments
import math
from operator import index

PI=math.pi
r=10
print(f"A gömb felszíne A={4*r**2*PI:.2f}")
print(f"A gömb térfogata V={4*r**3*PI/3:.2f}")

#2. Pitagorasz tétel
a=3
b=4
print(f"Pitagorasz tétel cc={a**2+b**2:.2f} c={math.sqrt(25)}")

#3. Egy burkoló úgy számolja ki a csempeszükségletet: a területe helység+10%
#Ára négyzetméterre 1500Ft
#Mennyit kell fizetni egy 3*3*2 méteres fürdő burkoláshoz?
a=3
b=3
c=2

print(f"T1={a*b:.0f}")
print(f"T2={a*b*c:.0f}")
print(f"T={9+18:.0f}")
print(f"T össz={27*1.1:.1f}")
print(f"Burkolás ára={29.7*1500:.0f}Ft")

#4. Henger felszín és térfogata
r=10
m=10
PI=math.pi

print(f"Henger felszíne A={2*r**2*PI+2*r*PI*m:.2f}")
print(f"Henger térfogata V={r**2*PI*m:.2f}")

#5. Másodfokú egyenlet megoldásai
import math
a=1
b=2
c=0

delta=b*b-4*a*c
x1=(-1*b+math.sqrt(delta)) /2*a
x2=(-1*b-math.sqrt(delta)) /2*a

print(f"A megoldások: %d %d" % (x1, x2))