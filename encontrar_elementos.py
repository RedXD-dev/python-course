cosa=0
lista=[]
flag=False
contador=-1
uno=1
while cosa!=-1:
    cosa=int(input("Ingresa un numero (o escribe '-1' para terminar):"))
    lista.append(cosa)
lista.remove(-1)
numero=int(input("Ingresa un numero:"))
for a in lista:
    if numero==a:
        flag=True
if flag:
    for e in lista:
        contador+=uno
        if numero==e:
            uno-=1
    print(f"El numero fue encontrado en el indice {contador}")
else:
    print("El numero no fue encontrado en la lista")
