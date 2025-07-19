matris=[
    ["🔲","🔲","🔲"],
    ["🔲","🔲","🔲"],
    ["🔲","🔲","🔲"]
]
#para el while
cosa=0
numero=0
tres=0
diez=0
#Para las coordenadas
contador=0
listas_1=1
#
simbolo_actual="✘"
simbolo_diferente="●"
simbolo=""
while cosa!=-1:
    print(matris[0], "fila 0")
    print(matris[1], "fila 1")
    print(matris[2], "fila 2")
    print("['0' , '1' , '2' ] columna")
    posicion=input(f"Jugador {simbolo_actual},Escriba en que cordendas va a colocar su ficha (ejemplo: '1,2'): ")
    #position = 3,1
    
    if int(posicion[0])>=0 and int(posicion[0])<=2 and int(posicion[2])>=0 and int(posicion[2])<=2: #Posicion valida  
        
   
        if matris[int(posicion[0])][int(posicion[2])] == "🔲": #aca valida si ya gano y coloca la ficha 
            matris[int(posicion[0])][int(posicion[2])] = simbolo_actual
            if matris[0][0]==simbolo_actual and matris[1][0]==simbolo_actual and matris[2][0]==simbolo_actual:#Valida la fila 0
                tres=3
            elif matris[0][1]==simbolo_actual and matris[1][1]==simbolo_actual and matris[2][1]==simbolo_actual:#Valida la fila 1
                tres=3
            elif matris[0][2]==simbolo_actual and matris[1][2]==simbolo_actual and matris[2][2]==simbolo_actual:#Valida la fila 2
                tres=3
            elif matris[0][0]==simbolo_actual and matris[0][1]==simbolo_actual and matris[0][2]==simbolo_actual:#Valida la columna 0
                tres=3
            elif matris[1][0]==simbolo_actual and matris[1][1]==simbolo_actual and matris[1][2]==simbolo_actual:#Valida la columna 1
                tres=3
            elif matris[2][0]==simbolo_actual and matris[2][1]==simbolo_actual and matris[2][2]==simbolo_actual:#Valida la columna 2
                tres=3
            elif matris[0][0]==simbolo_actual and matris[1][1]==simbolo_actual and matris[2][2]==simbolo_actual:#Valida la diagonal
                tres=3
            elif matris[2][0]==simbolo_actual and matris[1][1]==simbolo_actual and matris[0][2]==simbolo_actual:#Valida la diagonal
                tres=3
            simbolo=simbolo_actual
            simbolo_actual=simbolo_diferente
            simbolo_diferente=simbolo
            diez+=1
        else:
            print("Este lugar ya esta ocupado intentelo en otro")
        listas_1=1    
        if tres==3:
            cosa=-1
            print(f"El jugador {simbolo_diferente}, gano")
        elif diez==9:
            cosa=-1
            print("Nadie gano")
    else:
        print("Esta fuera de los limites intentalo de nuevo")
        posicion=input(f"Jugador {simbolo_actual},Escriba en que cordendas va a colocar su ficha (ejemplo: '1,3')")
 

print(matris[0], "fila 0")
print(matris[1], "fila 1")
print(matris[2], "fila 2")
print("['0' , '1' , '2' ] columna")