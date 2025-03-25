contador=1
lista=[]
cosa=0
while cosa!=-1:
    cosa=int(input("Ingresa un numero (o escribe '-1' para terminar):"))
    lista.append(cosa)
    contador+=cosa
lista.remove(-1)
print(f"la suma de la lista de {lista} es {contador}")