cosa=0
lista_duplicados=[]
lista_normal=[]
lista=[]
flag=False
while cosa!=-1:
    cosa=int(input("Escribe un numero (o escirbe '-1' para terminar): "))
    lista_duplicados.append(cosa)

lista_duplicados.remove(-1)
for number in lista_duplicados:
    for numero in lista_normal:
        if number == numero:
            flag=True

    if(flag == False):
        lista_normal.append(number)
    flag=False
print(f"Lista normal:{lista_duplicados}")
print(f"Lista sin duplicados:{lista_normal}")