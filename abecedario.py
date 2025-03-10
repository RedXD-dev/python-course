#Solicita al usuario una letra e imprime el resto del abecedario(Incluyendo la letra)
letra=input("Ingrese una letra:")
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
contador=0
for a in abecedario:
    if letra==a:
        contador+=1
    if contador==1:
        print(a , end="")
print()