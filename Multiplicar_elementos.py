cosa=0
lista=[]
lista_multiplicativa=[]

while cosa!=-1:
    cosa=int(input("Escribe un numero (o escribe '-1' para terminar):"))
    lista.append(cosa)
lista.remove(-1)
numero=int(input("Escribe un numero: "))
for i in lista:
    lista_multiplicativa.append(i*numero)
print(f"Lista normal:{lista}")
print(f"Lista con el numero {numero} multiplando:{lista_multiplicativa}")