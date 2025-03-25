cosa=0
lista=[]
lista_mayor=[]
while cosa!=-1:
    cosa=int(input("Ingresa un numero (o escribe '-1' para terminar):"))
    lista.append(cosa)
lista.remove(-1)
numero=int(input("Ingresa un numero:"))
for i in lista:
    if numero < i:
        lista_mayor.append(i)
print(f"Lista:{lista}, Limite {numero}, Numeros maypres que el limite:{lista_mayor}")