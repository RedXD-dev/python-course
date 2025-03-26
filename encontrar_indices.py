cosa=0
lista=[]
contador=0
lista2=[]
while cosa!=-1:
    cosa=int(input("Escribe un numero (o escribe '-1' para terminar):"))
    lista.append(cosa)
lista.remove(-1)
numero=int(input("escribe un numero:"))
for i in lista:
    if i==numero:
        lista2.append(contador)
    contador+=1
print(f"Lista: {lista}, Numero: {numero}, index encontrados: {lista2}")