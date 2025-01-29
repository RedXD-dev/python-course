#solicta un texto al usuario e imprime la suma de las letras-ascii
texto=input("Ingrese un texto:")
contador=0
for i in texto:
    contador+=ord(i)
    print(ord(i))
    
print(f"La suma del {texto} es: {contador}")