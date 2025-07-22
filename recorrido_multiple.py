import time
#el mapa sera una matriz 10*10 solicita al usuario la direccion y despues el numero de casillas a moverse 
#si el muñeco no se puede mover tantas casillas como se le indico solo marca error 
def matriz_original():
    matriz=[
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
    ]
    return matriz

def imprimir(matriz):
    filas=len(matriz)

    for i in range(0,filas):
        print(matriz[i])


def validacion(posicion):
    return posicion >= 0 and posicion <= 9

def up(fila):
    if validacion(fila -1):
        fila-=1
    else:
        print("error")
    return fila

def down(fila):
    if validacion(fila  +1):
        fila+=1
    else:
        print("error")
    return fila

def left(columna):
    if validacion(columna -1):
        columna-=1
    else:
        print("error")
    return columna

def right(columna):
    if validacion(columna +1):
        columna+=1
    else:
        print("error")

    return columna




#El codigo de arriba no conoce el codigo de abajo



cosa=1
mapa = matriz_original()
casillas=0
fila=0
columna=0
mapa[fila][columna] = "👻"
imprimir(mapa)
while cosa!=-1:
    direccion=input("Ingrese 'w' =  ⬆  o 'a' =  ⬅  o 's' =  ⬇  o 'd' =  ⮕  o 'fin' = terminar: ")

    if direccion == 'fin':
        print("Gracias")
        cosa=-1
    else:
        numero_pasos = int(input("# de pasos: "))
        if direccion == 'w':
            for a in range(0, numero_pasos):
                fila = up(fila)
                mapa = matriz_original()
                mapa[fila][columna] = "👻"
                imprimir(mapa)
                print("")
                time.sleep(1)

        elif direccion == 'a':
            for e in range(0, numero_pasos):
                columna = left(columna)
                mapa = matriz_original()
                mapa[fila][columna] = "👻"
                imprimir(mapa)
                print("")
                time.sleep(1)


        elif direccion == 's':
            for i in range(0,numero_pasos):
                fila = down(fila)
                mapa = matriz_original()
                mapa[fila][columna] = "👻"
                imprimir(mapa)
                print("")
                time.sleep(1)


        elif direccion == 'd':
            for u in range(0,numero_pasos):
                columna = right(columna)
                mapa = matriz_original()
                mapa[fila][columna] = "👻"
                imprimir(mapa)
                print("")
                time.sleep(1)
