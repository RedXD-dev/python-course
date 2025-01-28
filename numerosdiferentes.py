#solicita al usuario numeros hasta que coloque '-1'
#muestra en una lista lo numeros que se repitan solo dos veces
#1, 3, 2, 5, 4, 1, 3
#respuesta:1,3
contador=0
index=0
lista=[]
number=0
index2=0
lista_de_duplicados=[]
contador2=0
while number!=-1:
    number=int(input("Ingrese un numero (o escribe '-1' para terminar):"))
    lista.append(number)
lista.remove(-1)
for a in lista:
    for p in lista:
        if a==lista[index]:
            contador+=1
        index+=1
        #contador == 2
    for m in lista_de_duplicados:
        if a==p:
            contador2+=1
    if contador2==0:
        lista_de_duplicados.append(a)
        
            
    

    contador=0
    contador2=0 
    index=0
print(lista_de_duplicados)


num = 2
lista = [1,2,3]

for p in lista:
    if num ==p:
        contador2+=1

if contador2==0:
    lista.append(num)