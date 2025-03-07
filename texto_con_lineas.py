#texto=hola
#print(h-o-l-a)
texto=input("Ingrese un texto: ")
contador=len(texto)-1

for a in texto:
    print(a,end="")
    
    if contador!=0:
        print("-",end="")

    contador-=1

print("")