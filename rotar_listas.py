cosa=""
lista=[]
lista_invertida=[]
numero=-1
while cosa!="-1":
    cosa=input("Ingresa un numero (o escribe '-1' para terminar):")
    lista.append(cosa)
    numero+=1
lista.remove("-1")
contador=int(input("Escribe un numero: "))+1
for a in lista:
    if contador==numero:
        contador=0
    lista_invertida.append(lista[contador])
    contador+=1
print(lista)
print(lista_invertida)