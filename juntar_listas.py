cosa=""
lista=[]
while cosa!="fin":
    cosa=input("Ingresa una palabra (o escribe 'fin' para terminar):")
    lista.append(cosa)
lista.remove("fin")
for i in lista:
    print(i," ",end="")
print("")