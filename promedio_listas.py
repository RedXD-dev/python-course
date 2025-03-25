numeros=0
promedio=0
contador=0
suma=0
lista=[]
while numeros!=-1:
    numeros=float(input("Ingresa un numero (o escribe '-1' para terminar):"))
    lista.append(numeros)
lista.remove(-1)
for a in lista:
    contador+=1
    suma+=a
promedio=suma/contador
print(f"El promedio de la lista {lista} es {promedio}")