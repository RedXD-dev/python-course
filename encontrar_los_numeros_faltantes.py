number=int(input("escribe el tamaño de la lista:"))
contador3=-1
lista=[]
lista2=[]
for a in range(number):
    lista.append(0)
lista.append(0)
number1=0
while number1!='-1':
    number1=(input("ingrese un numero (o esrcibe '-1' para terminar)"))
    if number1!='-1':
        lista[int(number1)]+=1
for i in lista:
    contador3+=1
    if i==0:
        lista2.append(contador3)
print(f"los numeros que no aparecen son:{lista2}")