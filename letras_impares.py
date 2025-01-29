#solicita un texto al usuario
#E imprime las letras que estan el indice impar
texto=input("Ingrese un texto:")
index=0
for i in texto:
    if index %2!=0:
        print(i)
    index+=1