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
while lugar!="fin":
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
    lugar=input("Ingrese 'l' = ← o 'u' = ↑ o 'r' = → o 'b' = ↓ o 'fin' para terminar: ")
    if lugar=="l":
        if columna_futura!=0:
            columna_futura-=1
        else:
            print("Por aqui no se puede pasar, intenta ir a otro lado")
    elif lugar=="u":
        if fila_futura!=0:
            fila_futura-=1
        else:
            print("Por aqui no se puede pasar, intenta ir a otro lado")
    elif lugar=="b":
        if fila_futura!=4:
            fila_futura+=1
        else:
            print("Por aqui no se puede pasar, intenta ir a otro lado")
    elif lugar=="r":
        if columna_futura!=4:
            columna_futura+=1
        else:
            print("Por aqui no se puede pasar, intenta ir a otro lado")

    if matrices[fila_futura][columna_futura]!= "♖":
        fila=fila_futura
        columna=columna_futura
    else:
        fila_futura=fila
        columna_futura=columna
        print("Por aqui no se puede pasar, intenta ir a otro lado")
    matrices[fila][columna]="♟"
