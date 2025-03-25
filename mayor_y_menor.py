numero=0
lista=[]
contador_menor=10000000
contador_mayor=0
while numero!=-1:
    numero=int(input("Ingrese un numero (o escribe '-1' para terminar):"))
    lista.append(numero)
lista.remove(-1)
for i in lista:
    if contador_menor>i:
        contador_menor=i
    elif contador_mayor<i:
        contador_mayor=i
print(f"{lista} Maximo:{contador_mayor} y Minimo {contador_menor}")