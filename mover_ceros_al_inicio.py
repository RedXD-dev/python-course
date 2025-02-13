number=0
contador=0
lista=[]
lista2=[]
lista3=[]
while number!=-1:
    number=int(input("Ingrese un numero (o escribe '-1' para terminar):"))
    lista.append(number)
lista.remove(-1)
for a in lista:
    if a==0:
        contador+=1
for e in range(contador):
    lista2.append(0)
for i in lista:
    if i!=0:
        lista2.append(i)
print(lista)
print(lista2)