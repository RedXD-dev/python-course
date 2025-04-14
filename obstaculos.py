matrices=[
    ["♟","_","♖","_","_"],
    ["_","_","_","_","♖"],
    ["♖","_","_","_","_"],
    ["_","_","_","♖","_"],
    ["_","♖","_","_","_"]
]
fila=0
columna=0
fila_futura=0
columna_futura=0
lugar=""
contador=-1
contador_futuro=-1
contador_normal=0
while lugar != repr("fin"):
    print(matrices[0])
    print(matrices[1])
    print(matrices[2])
    print(matrices[3])
    print(matrices[4])
    print(fila_futura,columna_futura)
    matrices=[
    ["_","_","♖","_","_"],
    ["_","_","_","_","♖"],
    ["♖","_","_","_","_"],
    ["_","_","_","♖","_"],
    ["_","♖","_","_","_"]
    ]
    lugar=repr(input("Ingrese '⬅' = ← o '⬆' = ↑ o '⮕' = → o '⬇' = ↓ o 'fin' para terminar: "))
    if (lugar == repr('\x1b[D')):
        if columna_futura!=0:
            columna_futura-=1
        else:
            print("Por aqui no se puede pasar, intenta ir a otro lado")
    elif (lugar == repr('\x1b[A')):
        if fila_futura!=0:
            fila_futura-=1
        else:
            print("Por aqui no se puede pasar, intenta ir a otro lado")
    elif (lugar == repr('\x1b[B')):
        if fila_futura!=4:
            fila_futura+=1
        else:
            print("Por aqui no se puede pasar, intenta ir a otro lado")
    elif (lugar == repr('\x1b[C')):
        if columna_futura!=4:
            columna_futura+=1
        else:
            print("Por aqui no se puede pasar, intenta ir a otro lado")
    contador_futuro+=1
    if matrices[fila_futura][columna_futura]!= "♖":
        fila=fila_futura
        columna=columna_futura
        contador_normal=contador_futuro
    else:
        fila_futura=fila
        columna_futura=columna
        contador_futuro=contador_normal
        print("Por aqui no se puede pasar, intenta ir a otro lado")
    matrices[fila][columna]="♟"
    contador+=1
print(f"Te moviste {contador} veces")
print(f"Te moviste sin chocar {contador_normal} veces")