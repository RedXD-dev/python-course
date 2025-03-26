cosa=0
contador=0
lista=[]
while cosa!=-1:
    cosa=int(input("Escribe un numero (o escribe '-1' para terminar): "))
    lista.append(cosa)
lista.remove(-1)
numero=int(input("Escribe un numero: "))
for i in lista:
    if numero>i:
        contador+=1
print(f"Lista:{lista}, Numero:{numero}, veces que fue mayor el numero:{contador}")