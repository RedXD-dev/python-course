#Solicita al usuario una cifra y suma sus digitos
#Ejemplo=585
#5+8+5=18
numero=input("Ingrese un numero y sumare sus digitos:")
contador=-1
contador_resultado=0
for a in numero:
    contador+=1
    contador_resultado+=int(a)
for e in numero:
    print(e,end="")
    if contador!=0:
        print("+",end="")
        contador-=1
    elif contador==0:
        print("=",end="")
print(contador_resultado)