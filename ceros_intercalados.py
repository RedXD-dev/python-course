lista=[]
lista2=[]
number=0
contador=0
while number!=-1:
    number=int(input("Ingrese un numero (o escribe '-1' para terminar)"))
    lista.append(number)
lista.remove(-1)
for a in lista:
    if a==0:
        contador+=1
    elif a!=0:
        lista2.append(a)
for e in lista2:
    print(e,",",end="")
    if  contador>0:
        print(0,",",end="")
        contador-=1
for i in range(contador):
    print(0,",",end="")
print()