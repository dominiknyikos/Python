urtartalom=int(input("Üzemanyagtartály űrtartalma (l): "))
teljes=int(input("Teljes tankkal megtett út hossza (km): "))
fogyasztas=round((urtartalom/teljes)*100,1)

if fogyasztas<6.5:
    print(f"Az ön autójának fogyasztása alacsony: {fogyasztas}/100km")
elif fogyasztas<8.5:
    print(f"Az ön autójának fogyasztása átlagos: {fogyasztas}/100km")
else:
    print(f"Az ön autójának fogyasztása magas: {fogyasztas}/100km")