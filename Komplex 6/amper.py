n=int(input("Add meg, hogy a futár mennyi ételt szállított ki a hónapban: "))
m=int(input("Add meg, hogy mennyi mosolygós fejet kapott: "))
szazalek=round((m/n)*100)

print(f"{szazalek}%")

bonusz=0
if szazalek>=25 and szazalek<50:
    bonusz=50000
elif szazalek>=50 and szazalek<75:
    bonusz=100000
elif szazalek>=75 and szazalek<90:
    bonusz=150000
else:
    bonusz=200000
print(f"A bónusz mértéke: {bonusz}Ft")