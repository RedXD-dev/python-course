#Crea una matris de 10*10 
#Solicita al usuario fila y columna y caracter
#Terminar de preguntar hasata que fila sea -1
#Si el usuario elige una casilla ocupada no remplezar el valor y mostra de un error 
matris=[
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
cosa=0
numero=0
while cosa!=-1:
    print("Fila 0",matris[0])
    print("Fila 1",matris[1])
    print("Fila 2",matris[2])
    print("Fila 3",matris[3])
    print("Fila 4",matris[4])
    print("Fila 5",matris[5])
    print("Fila 6",matris[6])
    print("Fila 7",matris[7])
    print("Fila 8",matris[8])
    print("Fila 9",matris[9])
    print("       ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ]")
    fila=int(input("Escriba la fila: "))
    while numero!=-1:
        if fila>9:
            print("Esta fuera de los limites intenta con otro numero")
            fila=int(input("Escriba la fila:"))
        else:
            numero=-1
    numero=0
    columna=int(input("escriba la columna: "))
    while numero!=-1:
        if columna>9:
            print("Esta fuera de los limites intenta con otro numero")
            columna=int(input("escriba la columna: "))
        else:
            numero=-1
    numero=0
    caracter=input("Escriba el caracter (que no sea el mismo que '⬛')")
    while numero!=-1:
        if caracter=="⬛":
            print("Intente con otro caracter")
            caracter=input("Escriba el caracter (que no sea el mismo que '⬛')")
        else:
            numero=-1
    if matris[fila][columna]=="⬛":
        matris[fila][columna]=caracter
    else:
        print("Ese espacio ya esta ocupado intente con otro ")
    cosa=int(input("Escibe '-1' para terminar o escriba cualquier numero para continuar: "))
print("Gracias")
print("Fila 0",matris[0])
print("Fila 1",matris[1])
print("Fila 2",matris[2])
print("Fila 3",matris[3])
print("Fila 4",matris[4])
print("Fila 5",matris[5])
print("Fila 6",matris[6])
print("Fila 7",matris[7])
print("Fila 8",matris[8])
print("Fila 9",matris[9])
print("       ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ]")