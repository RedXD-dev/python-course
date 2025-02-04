cosa=0
contador=0
contador1=0
contador2=0
contador3=100000000
lista=[]
lista2=[]
while cosa!=-1:
    cosa=int(input("Ingrese un numero (o escribe '-1' para terminar):"))
    lista.append(cosa)
lista.remove(-1)
for a in lista:
    if a>contador:
        contador=a    
for e in lista:
    contador1=contador-e
    if contador1<contador3 and contador1!=0:
        contador2=e
        contador3=contador1
print(f"El segundo numero mas grande la lista de {lista} es {contador2}")