#Solicita al usuario una letra e imprime el resto del abecedario(Incluyendo la letra)
letra=input("Ingrese una letra:")
abecedario="abcdefghijklmnopqrstuvwxyz"
contador=1
contador2=-1
contador3=0
for a in abecedario:
    contador3+=1
    contador2+=contador
    if letra==a:
        contador-=1
for e in abecedario[contador2:contador3]:
    print(e ,end="")
print("")