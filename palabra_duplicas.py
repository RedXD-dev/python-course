#solicita una lista de palabras hasta que el usuario escriba stop
#perro, gato, coneejo, perro, lombriz
# gato, conejo y lombriz
contador=0
lista=[]
lista_no_duplicados=[]
lista_duplicados=[]
contador2=0
palabra=""
while palabra!= "fin":
    palabra=input("Ingrese una palabra (o escribe 'fin' para terminar):")
    lista.append(palabra)

    #contar cuantas veces aparecen las palabras en las listas
    for a in lista_no_duplicados:
        if a == palabra:
            contador+=1

    for e in lista_duplicados:
        if e == palabra:
            contador2+=1

    if contador==0 and contador2==0:
        lista_no_duplicados.append(palabra)
    
    if contador!=0:
        lista_no_duplicados.remove(palabra)
        lista_duplicados.append(palabra)
    
    contador=0
    contador2=0
lista.remove("fin")
lista_no_duplicados.remove("fin")
print(f"La lista de {lista} sin duplicados es: {lista_no_duplicados}")