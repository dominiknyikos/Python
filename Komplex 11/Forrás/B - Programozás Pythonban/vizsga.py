egysegar=int(input("Vizsga egységára: "))
darabszam=int(input("Darabszám: "))
fizetendo=(egysegar*darabszam)+1000

print(f"Fizetendő összeg: {fizetendo} Ft")

if fizetendo>=8000:
    print(f"Kedvezményes ár: {round(fizetendo*0.88)} Ft")
else:
    print(f"Kedvezményes ár: {round(fizetendo*0.92)} Ft")