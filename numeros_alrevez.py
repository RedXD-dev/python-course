#Solicita al usuario un un numero e imprimelo de derecha a izquierda
#Ejemplo=347
#743
numero=input("Ingrese un numero:")
contador=-1
lista=[]
for a in numero:
    lista.append(contador)
    contador+=1
for e in numero:
    lista.pop(contador)
    lista.insert(contador,e)
    contador-=1
for i in lista:
    print(i,end="")
print()