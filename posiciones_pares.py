lista=[]
contador=0
contador2=1
lista2=[]
number=0
while number!=-1:
    number=int(input("ingrese un numero (o escribe '-1' para terminar)"))
    lista.append(number)
lista.remove(-1)
for i in lista:
    if contador%2==0 :
        lista2.append((lista[contador]))
    contador+=1
for p in lista2:
    contador2*=p


print(f"la lista de {lista} sus multiplaciones en las posiciones pares es {contador2} (los numeros en las posicones pares son {lista2}:")