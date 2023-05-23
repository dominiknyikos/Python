magassag=int(input("Magasság: "))
sugar=int(input("Sugár: "))

def henger_terfogatszamitas(a,b):
      V=a*b**2*3.14
      return V

if henger_terfogatszamitas(magassag,sugar)<5:
    print("kicsi hordó")
elif 5<=henger_terfogatszamitas(magassag,sugar)<7.5:
    print("közepes hordó")
else:
    print("nagy hordó")