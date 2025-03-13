#Solicita al usuario un texto y muesta cuantas vocales hay
texto=input("Ingresa un texto:")
a=0
e=0
i=0
o=0
u=0
for b in texto:
    if b=="a":
        a+=1
    elif b=="e":
        e+=1
    elif b=="i":
        i+=1
    elif b=="o":
        o+=1
    elif b=="u":
        u+=1
print(f"En el texto {texto} hay {a}=a, {e}=e, {i}=i, {o}=o y {u}=u")