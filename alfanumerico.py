texto=input("Ingrese un texto alfanumerico:")
for a in texto:
    contador=ord(a)-ord("a")
    if contador>=0 and contador<=25:
        print(a,end="")
print()