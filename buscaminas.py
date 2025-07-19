matrices_bombas=[
    ["🔲","🔳","🔲","🔳","🔲","🔳"],
    ["🔳","💣","🔳","🔲","💣","🔲"],
    ["🔲","🔳","🔲","🔳","🔲","🔳"],
    ["🔳","🔲","🔳","💣","🔳","🔲"],
    ["💣","🔳","🔲","🔳","🔲","🔳"],
    ["🔳","🔲","🔳","💣","🔳","🔲"],
    ["🔲","🔳","🔲","🔳","🔲","🔳"],
    ["🔳","💣","🔳","🔲","🔳","🔲"],
    ["🔲","🔳","🔲","💣","🔲","💣"]
]
matrices=[
    ["🔲","🔳","🔲","🔳","🔲","🔳"],
    ["🔳","🔲","🔳","🔲","🔳","🔲"],
    ["🔲","🔳","🔲","🔳","🔲","🔳"],
    ["🔳","🔲","🔳","🔲","🔳","🔲"],
    ["🔲","🔳","🔲","🔳","🔲","🔳"],
    ["🔳","🔲","🔳","🔲","🔳","🔲"],
    ["🔲","🔳","🔲","🔳","🔲","🔳"],
    ["🔳","🔲","🔳","🔲","🔳","🔲"],
    ["🔲","🔳","🔲","🔳","🔲","🔳"] 
]
posicion=0
contador=0#🟩💣
contador_fila=0
contador_columna=0
while contador!=-1:
    print(matrices[0],"fila 0")
    print(matrices[1],"fila 1")
    print(matrices[2],"fila 2")
    print(matrices[3],"fila 3")
    print(matrices[4],"fila 4")
    print(matrices[5],"fila 5")
    print(matrices[6],"fila 6")
    print(matrices[7],"fila 7")
    print(matrices[8],"fila 8")
    print("['0' , '1' , '2' , '3' , '4' , '5' ] = ('son las columnas')")
    posicion1=int(input("Ingrese la fila: "))
    posicion2=int(input("Ingrese la columna: "))
    if matrices_bombas[posicion1][posicion2]=="💣":
        print("perdiste")
        contador=-1
    elif contador!=-1:
        matrices[posicion1][posicion2]="🟩"
        if posicion1!=8:
            posicion1+=1
            if matrices_bombas[posicion1][posicion2]=="💣":
                contador+=1       
        posicion1-=1
    if posicion1!=0:
        posicion1-=1
        if matrices_bombas[posicion1][posicion2]=="💣":
            contador+=1
    posicion1+=1

    if posicion2!=8:
        posicion2+=1
        if matrices_bombas[posicion1][posicion2]=="💣":
            contador+=1
    posicion2-=1
    if posicion2!=0:
        posicion2-=1
        if matrices_bombas[posicion1][posicion2]=="💣":
            contador+=1
        posicion2+=1
    if contador>=0:
        print(f"Hay {contador} bombas cercas")