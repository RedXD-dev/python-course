#🚘
f0=["🚘","_","_","_","_"]
f1=["_","_","_","_","_"]
f2=["_","_","_","_","_"]
f3=["_","_","_","_","_"]
f4=["_","_","_","_","_"]
fila=0
columna=0
while dir!="fin":
    print(f0)
    print(f1)
    print(f2)
    print(f3)
    print(f4)
    #Reinicio de mapa
    f0=["_","_","_","_","_"]
    f1=["_","_","_","_","_"]
    f2=["_","_","_","_","_"]
    f3=["_","_","_","_","_"]
    f4=["_","_","_","_","_"]
    #Se captura la nueva direccion
    dir=input("Ingrese 'l' = ← o 'u' = ↑ o 'r' = → o 'b' = ↓ o 'fin' para terminar: ")

    #Este if captura cuando va a la izquierda
    if dir=="l":
        if columna!=0:
            columna-=1
        else:
            print("Fuera de alcance")
    #Este elif captura cuando va hacia arriba
    elif dir=="u":
        if fila!=0:
            fila-=1
        else:
            print("Fuera de alcance")
    #Este elif captura cuando va a la derecha
    elif dir=="r":
        if columna!=4:
            columna+=1
        else:
            print("Fuera de alcance")
    #Este elif captura cuando va hacia abajo
    elif dir=="b":
        if fila!=4:
            fila+=1
        else:
            print("Fuera de alcance")
    elif dir=="fin":
        print("Gracias")
    else:
        print("Invalido")
    #Esta seccion de if's nos ayuda a decidir que lista alterar
    if fila==0:
        f0[columna] = "🚘"
    elif fila==1:
        f1[columna] = "🚘"
    elif fila==2:
        f2[columna] = "🚘"
    elif fila==3:
        f3[columna] = "🚘"
    elif fila==4:
        f4[columna] = "🚘"