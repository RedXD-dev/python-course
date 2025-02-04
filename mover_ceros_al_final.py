lista=[]
lista2=[]
index=0
cosa=0
while cosa!= '-1':
    cosa=input("Ingrese un numero (o escribe '-1' para terminar):")
    lista.append(cosa)

lista.remove('-1')
contador=len(lista)
contador1=0
for a in lista:
    if int(a)!=0:
        lista2.append(a)
    else:
        contador1+=1
for e in range(contador1):
    lista2.append('0')
print(f"La lista de {lista} moviendo los '0' hasta el final queda asi:{lista2}")
