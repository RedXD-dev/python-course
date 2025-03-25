numero=""
lista=[]
index=-2
lista_invertida=[]
while numero!="-1":
    numero=input("Ingresa un numero (o escribe '-1' para terminar):")
    lista.append(numero)
    index+=1
lista.remove("-1")
for a in lista:
    lista_invertida.append(lista[index])
    index-=1
print(f"Lista original:{lista}")
print(f"Listainvertida:{lista_invertida}")