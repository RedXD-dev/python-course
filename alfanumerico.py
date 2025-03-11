texto=input("Ingrese un texto alfanumerico:")
for a in texto:
    contador=ord(a)-ord("A")
    if contador>=0 and contador<=25:
        print(a,end="")
    elif contador>=32 and contador<=57:
        print(a,end="")
print()