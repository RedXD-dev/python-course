lista=[]
lista1=[0,0,0,0,0,0,0,0,0,0]
number=0
contador=0
while number!='-1':
    number=(input("Ingrese un numero '0-9' (o escribe '-1' para terminar):"))
    lista.append(number)
lista.remove('-1')
for a in lista:
    cosa=ord(a)-ord("0")
    lista1[cosa]+=1
for e in lista:
    cosa=ord(e)-ord("0")
    if lista1[cosa]==1:
        contador+=cosa
print(f"La suma de los numeros unicos de la lista de {lista} es: {contador}")