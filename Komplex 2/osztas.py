a=int(input("Kérlek add meg az első számot: "))
b=int(input("Kérlek add meg a második számot: "))
osztas_1=a/b
osztas_2=b/a

elso=False
masodik=False
if a%b==0 and b%a==0:
    print(f"{osztas_1} egész és {osztas_2} egész")
elif a%b==0 and b%a!=0:
    print(f"{osztas_1} egész és {osztas_2:.2f} nem egész")
elif a%b!=0 and b%a==0:
    print(f"{osztas_1:.2f} nem egész és {osztas_2} egész")
elif a%b!=0 and b%a!=0:
    print(f"{osztas_1:.2f} nem egész és {osztas_2:.2f} nem egész")
print(f"Az a {(a/b)*100}%-a b-nek, és a b {(b/a)*100}%-a a-nak.")