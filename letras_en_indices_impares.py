#ingresa un texto e imprime las letras que estan en posiciones impares
#texto=hola
#      01234
#print(o-a)
texto=input("Ingrese un texto: ")
index=0
for a in texto:
    if index%2!=0:
        print(a,"",end="")
    index+=1
print("")