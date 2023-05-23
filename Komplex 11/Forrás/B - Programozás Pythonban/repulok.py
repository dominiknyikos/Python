class Repulo():
    def __init__(self,s):
        sor=s.split(";")
        self.tipus=sor[0]
        self.ev=int(sor[1])
        self.sebesseg=int(sor[2])
        self.fesztav=float(sor[3])
lista=[]
with open("repulok.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(Repulo(i.strip()))
f.close()

print(f"Repülőgépek száma: {len(lista)}")

print("Boeing repülők:")
for i in lista:
    if "Boeing".upper() in i.tipus.upper():
        print(i.tipus)

ki=open("sebesseg.txt", "w", encoding="utf-8")
also=int(input("Alsó határ: "))
felso=int(input("Felső határ: "))
repulok=[]
if also>felso:
    print("Hibás bevitel")
else:
    for i in lista:
        if also<=i.sebesseg<=felso and 1950<i.ev:
            repulok.append(i.tipus)
            ki.write(f"{i.tipus} \n")
    if len(repulok)==0:
        ki.write("Nem található ilyen sebességű repülő.")
    else:
        print(f"A megadott sebességű, 1950 után indított repülők száma: {len(repulok)}")

atvalt=0.62
feletti=[]
def KmhToMph(atvalt,ertek):
    return round(ertek/atvalt,2)

for i in lista:
    if i.fesztav>=40:
        feletti.append(KmhToMph(atvalt,i.sebesseg))
print(f"Legalább 40-es fesztávú repülők átlagsebessége: {round(sum(feletti)/len(feletti),1)} mph")