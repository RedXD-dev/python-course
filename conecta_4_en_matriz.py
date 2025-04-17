print()
matriz=[
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "]
]
contador=0
fila_actual=0
contador_izquierda=0
contador_derecha=0
contador_arriba=0
contador1=0
signo_actual="◉"
signo_diferente="✖"
signo=""

while contador<4:
    fila=6
    print("0",matriz[0])
    print("1",matriz[1])
    print("2",matriz[2])
    print("3",matriz[3])
    print("4",matriz[4])
    print("5",matriz[5])
    print("6",matriz[6])
    print("  ['0', '1', '2', '3', '4', '5', '6']    (Los numero es para saber que posicion van)")
    jugador=int(input(f"Jugador {signo_actual}: Escriba en que columna va a insertar la ficha : "))

    while fila != -1:#sirve para colocar la ficha

        if jugador>6:
            print("Esta fuera de rango intenta otro numero menor")
            jugador=int(input(f"Jugador {signo_actual}: Escriba en que columna va a insertar la ficha : "))

        elif matriz[fila][jugador]==" ":
            matriz[fila][jugador]=signo_actual
            fila_actual=fila
            fila= -1

        elif matriz[fila][jugador]!=" ":
            fila-=1

            if fila==-1:
                print("Esta lleno intentanlo en otro lugar")
        

    contador1=jugador
    fila=fila_actual
    while jugador>=0 and matriz[fila_actual][jugador]!=" " and matriz[fila_actual][jugador]!= signo_diferente:
        jugador-=1
        contador_izquierda+=1

    jugador=contador1

    while jugador<=6 and matriz[fila_actual][jugador]!=" " and matriz[fila_actual][jugador]!= signo_diferente:
            jugador+=1
            contador_derecha+=1

    contador_derecha-=1
    jugador=contador1
    while fila<=6 and matriz[fila][jugador]!= signo_diferente:
        fila+=1
        contador_arriba+=1
    contador+=contador_derecha+contador_izquierda

    if contador>=4 :
        print(f"Gano el jugador {signo_actual}")

    elif contador_arriba>=4:
        print(f"Gano el jugador {signo_actual}")
        contador=contador_arriba

    else:
        contador=0
        contador_derecha=0
        contador_izquierda=0
        contador_arriba=0
        contador1=0
        
    signo=signo_actual
    signo_actual=signo_diferente
    signo_diferente=signo

print("0",matriz[0])
print("1",matriz[1])
print("2",matriz[2])
print("3",matriz[3])
print("4",matriz[4])
print("5",matriz[5])
print("6",matriz[6])
print("  ['0', '1', '2', '3', '4', '5', '6']    (Los numero es para saber que posicion van)")