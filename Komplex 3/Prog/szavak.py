szo_elso=input("Adj meg egy szót! ")
szo_masodik=input("Adj meg egy másik szót! ")

if len(szo_elso)>len(szo_masodik):
    print(f"A hosszabb szó: {szo_elso}")
elif len(szo_elso)<len(szo_masodik):
    print(f"A hosszabb szó: {szo_masodik}")
else:
    print(f"A két szó egyforma hosszú.")