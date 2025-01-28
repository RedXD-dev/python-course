contador_letra=122
texto1=input("Ingrese una plabar (ejemplo='jpklrskx'):")
for a in texto1:
    cosa=ord(a)
    if contador_letra>=cosa:
        contador_letra=cosa
print(f"La letra mas pequeña de {texto1} es {chr(contador_letra)}")