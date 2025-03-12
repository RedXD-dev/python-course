#Solicita al usuario un texto y solo imprime los caracteres especiales:
texto=input("Ingresa un texto: ")
for a in texto:
    contador=ord(a)-ord(" ")
    if contador>=16 and contador<=25:
        print("",end="")
    elif contador>=33 and contador<=58:
        print("",end="")
    elif contador>=65 and contador<=90:
        print("",end="")
    else:
        print(a,end="")
print()