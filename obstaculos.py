#Se tendran 5 listas de tamaño 5
#ahora en las listas van a ver obstaculos
fila_0=["♟","⛫","_","_","_"]
fila_1=["_","_","_","⛫","_"]
fila_2=["⛫","_","_","_","_"]
fila_3=["_","_","⛫","_","_"]
fila_4=["_","_","_","_","⛫"]
fila=0
columna=0
fila_futura=0
columna_futura=0
cosa=""
while cosa!="fin":
    print(fila_0)
    print(fila_1)
    print(fila_2)
    print(fila_3)
    print(fila_4)
    fila_0=["_","⛫","_","_","_"]
    fila_1=["_","_","_","⛫","_"]
    fila_2=["⛫","_","_","_","_"]
    fila_3=["_","_","⛫","_","_"]
    fila_4=["_","_","_","_","⛫"]
    cosa=input("Ingrese 'l' = ⬅ o 'u' = ⬆ o 'b' = ⬇  o 'r' = ⮕ o ingrese 'fin' para terminar: ")
    if cosa=="l":
        if columna_futura!=0:
            columna_futura-=1
        else:
            print("No se permite pasar por aqui")
    elif cosa=="u":
        if fila_futura!=0:
            fila_futura-=1
        else:
            print("No se permite pasar por aqui")
    elif cosa=="b":
        if fila_futura!=4:
            fila_futura+=1
        else:
            print("No se permite pasar por aqui")
    elif cosa=="r":
        if columna_futura!=4:
            columna_futura+=1
        else:
            print("No se permite pasar por aqui")

    if fila_futura==0:

        if fila_0[columna_futura] == "⛫":
            print("no se puede pasar por aqui")
            fila_futura = fila
            columna_futura = columna
            if fila==0:
                fila_0[columna] = "♟"
            elif fila==1:
                fila_1[columna] = "♟"
            elif fila==2:
                fila_2[columna] = "♟"
            elif fila==3:
                fila_3[columna] = "♟"
            elif fila==4:
                fila_4[columna] = "♟"
            

        else:
            fila = fila_futura
            columna = columna_futura
            fila_0[columna] = "♟"

    elif fila_futura==1:

        if fila_1[columna_futura] == "⛫":
            print("no se puede pasar por aqui")
            fila_futura = fila
            columna_futura = columna
            if fila==0:
                fila_0[columna] = "♟"
            elif fila==1:
                fila_1[columna] = "♟"
            elif fila==2:
                fila_2[columna] = "♟"
            elif fila==3:
                fila_3[columna] = "♟"
            elif fila==4:
                fila_4[columna] = "♟"
            
        else:
            fila = fila_futura
            columna = columna_futura
            fila_1[columna] = "♟"

    elif fila_futura==2:

        if fila_2[columna_futura] == "⛫":
            print("no se puede pasar por aqui")
            fila_futura = fila
            columna_futura = columna 
            if fila==0:
                fila_0[columna] = "♟"
            elif fila==1:
                fila_1[columna] = "♟"
            elif fila==2:
                fila_2[columna] = "♟"
            elif fila==3:
                fila_3[columna] = "♟"
            elif fila==4:
                fila_4[columna] = "♟"

        else:

            fila = fila_futura
            columna = columna_futura
            fila_2[columna] = "♟"

    elif fila_futura==3:

        if fila_3[columna_futura] == "⛫":
            print("no se puede pasar por aqui")
            fila_futura = fila
            columna_futura = columna
            if fila==0:
                fila_0[columna] = "♟"
            elif fila==1:
                fila_1[columna] = "♟"
            elif fila==2:
                fila_2[columna] = "♟"
            elif fila==3:
                fila_3[columna] = "♟"
            elif fila==4:
                fila_4[columna] = "♟"
            
        else:
            fila = fila_futura
            columna = columna_futura
            fila_3[columna] = "♟"

    elif fila_futura==4:

        if fila_4[columna_futura] == "⛫":
            print("no se puede pasar por aqui")
            fila_futura = fila
            columna_futura = columna
            if fila==0:
                fila_0[columna] = "♟"
            elif fila==1:
                fila_1[columna] = "♟"
            elif fila==2:
                fila_2[columna] = "♟"
            elif fila==3:
                fila_3[columna] = "♟"
            elif fila==4:
                fila_4[columna] = "♟"
            
        else:
            fila = fila_futura
            columna = columna_futura
            fila_4[columna] = "♟"