#Solicita al usuario una letra e imprime el resto del abecedario(Incluyendo la letra)
letra=input("Ingrese una letra:")
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
contador=-1
contador2=1
contador3=len(abecedario)
for a in abecedario:
    contador+=contador2
    if ord(letra)-ord(a)==0:
        contador2-=1
for e in abecedario[contador:contador3]:
    print(e,end="")
print()