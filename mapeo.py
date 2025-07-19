#Solicita al usuario introducir 5 cordenadas (Fila, columna)
#Y dibujalas en un matriz
#la matriz sera de 5*5 ⬛ ⬜
matriz=[
        ["⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛"]
]
cosa=""
limite=""
while cosa!="no":
    print("Fila 0",matriz[0])
    print("Fila 1",matriz[1])
    print("Fila 2",matriz[2])
    print("Fila 3",matriz[3])
    print("FIla 4",matriz[4])
    print("       ['0' , '1' , '2' , '3' , '4' ]")
    cordenadas_fila=int(input("Escriba la fila:"))
    while limite!=-1:
        if cordenadas_fila>4:
            print("Esta fuera de rango")
            cordenadas_fila=int(input("Escriba la fila: "))
        else:
            limite=-1
    limite=0
    cordenadas_columna=int(input("Escirba la columna: "))
    while limite!=-1:
        if cordenadas_columna>4:
            print("esta fuera de rango")
            cordenadas_columna=int(input("esciba la columna:"))
        else:
            limite=-1
    limite=0
    if matriz[cordenadas_fila][cordenadas_columna]=="⬛":
         matriz[cordenadas_fila][cordenadas_columna]="⬜"
    cosa=input("Escriba 'no' para terminar o escibe cualquier cosa para terminar: ")
print("Gracias")
print("Fila 0",matriz[0])
print("Fila 1",matriz[1])
print("Fila 2",matriz[2])
print("Fila 3",matriz[3])
print("FIla 4",matriz[4])
print("       ['0' , '1' , '2' , '3' , '4' ]")