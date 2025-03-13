#Solicita al usuario una lista de materias 
#En otra lista solicita al usuario ingresar las calificacion
materia=()
calificacion=0
cosa=()
lista_materia=[]
lista_calificacion=[]
contador=-1
uno=1
contador2=0

while materia!="fin":
    materia=input("Ingrese una materia (o escribe 'fin' para terminar):")
    lista_materia.append(materia)
lista_materia.remove("fin")
contador3=len(lista_materia)

for a in lista_materia:
    calificacion=input("Ingrese una calificacion para una materia :")
    lista_calificacion.append(calificacion)

while cosa!="salir":
    cosa=input("Ingresa que materia quiere ver su calificacion (o ingrese 'salir' para terminar)")

    for b in lista_materia:
        contador+=uno
        contador2+=uno

        if cosa==b:
            print(b,",",lista_calificacion[contador])
            uno-=1

        elif contador2==contador3:
            print("Materia no encontrada")
    uno=1
    contador2=0
    contador=-1