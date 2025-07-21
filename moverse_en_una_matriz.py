#utiliza una matriz de 5*4 el jugador iniciara en la coordenada 0,0 
#a = izquierda, w = arriba , d = derecha, s = abajo
def fila_0(fila_actual):
    return fila_actual>=0 and fila_actual<=4

def columna_0(columna_actual):
    return columna_actual>=0 and columna_actual<=3

def up(fila):
    if fila_0(fila -1):
        fila-=1
    else:
        print("No se puede pasar por aqui")
    return fila

def down(fila):
    if fila_0(fila + 1 ):
        fila+=1
    else:
        print("No se puede pasar por aqui")
    return fila

def left(columna):
    if columna_0(columna -1):
        columna-=1
    else:
        print("No se puede pasar por aqui")
    return columna
        
def right(columna):
    if columna_0(columna+1):
        columna+=1
    else:
        print("No se puede pasar por aqui")
    return columna

matriz=[
    ["👻","⬜","⬜","⬜"],
    ["⬜","⬜","⬜","⬜"],
    ["⬜","⬜","⬜","⬜"],
    ["⬜","⬜","⬜","⬜"],
    ["⬜","⬜","⬜","⬜"]

]
cosa=0
coordenadas=[0,0]
while cosa!=-1:
    print(matriz[0],"fila 0")
    print(matriz[1],"fila 1")
    print(matriz[2],"fila 2")
    print(matriz[3],"fila 3")
    print(matriz[4],"fila 4")
    print("['0' , '1' , '2' , '3' ]")
    movimiento=input("Ingrese 'a' = ⬅  o 'w' = ⬆  o 's' = ⬇  o 'd' = ⮕  o 'fin' = Terminar: ")
    if movimiento=="fin":
        print("Gracias")
        cosa=-1
    else:
        if movimiento=="a":
            coordenadas[1] = left(coordenadas[1])
            matriz[coordenadas[0]][coordenadas[1]+1] = "⬜"
            matriz[coordenadas[0]][coordenadas[1]] = "👻"
        elif movimiento=="w":
            coordenadas[0] = up(coordenadas[0])
            matriz[coordenadas[0]+1][coordenadas[1]] = "⬜"
            matriz[coordenadas[0]][coordenadas[1]] = "👻"
        elif movimiento=="s":
            fila_anterior = coordenadas[0]
            coordenadas[0] = down(coordenadas[0])
            matriz[coordenadas[0]-1][coordenadas[1]] = "⬜"
            matriz[coordenadas[0]][coordenadas[1]] = "👻"
        elif movimiento=="d":
            coordenadas [1] = right(coordenadas[1])
            matriz[coordenadas[0]][coordenadas[1]-1] = "⬜"
            matriz[coordenadas[0]][coordenadas[1]] = "👻"
        
    print(coordenadas)
print(matriz[0],"fila 0")
print(matriz[1],"fila 1")
print(matriz[2],"fila 2")
print(matriz[3],"fila 3")
print(matriz[4],"fila 4")
print("['0' , '1' , '2' , '3' ]")