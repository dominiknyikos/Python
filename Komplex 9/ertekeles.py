pontszam=int(input("Adj meg egy számot: "))

if pontszam>=250:
    print(f"A versenyző elérte a továbbjutási határt! ({pontszam} pont - {(pontszam/500)*100}%)")
else:
    print("A versenyző nem érte el a továbbjutási határt!")