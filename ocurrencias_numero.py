cosa=0
lista=[]
contador=0
numero=0
while cosa!=-1:
    cosa=int(input("Ingresa un numero (o escribe '-1' para terminar): "))
    lista.append(cosa)
lista.remove(-1)
numero=int(input("Dime un numero:"))
for i in lista:
    if numero==i:
        contador+=1
print(f"Lista:{lista} , Numero:{numero} , Veces encontradas:{contador}")