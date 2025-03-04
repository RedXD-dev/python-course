#Solicita al usuario un correo electronico y valida si es correcto
#Ejemplo:micorreo@midominio.com
#nombre+@+dominio+.com
correo=input("Ingrese un correo electronico:")
lista=[]
contador=-1
contador_1=-1
contador_2=0
contador_secundario2=1
contador_secundario=1
contador3=0
contador4=1
contador5=0
for a in correo:
    lista.append(a)

for e in lista:
    contador_1+=1
    if e!="@":
        contador+=contador_secundario
    if e=="@":
        contador_secundario-=1
for i in lista[contador+1:contador_1+1]:
    if i!=".":
        contador5+=contador4
    elif i==".":
        contador3+=1
        contador4-=1
    
if lista[contador_1-3]==".":
    contador_2+=1
if lista[contador_1-2]=="c":
    contador_2+=1
if lista[contador_1-1]=="o":
    contador_2+=1
if lista[contador_1]=="m":
    contador_2+=1
if contador>=1 and contador_secundario==0 and contador_2==4 and contador3==1 and contador5>=1:
    print("El correo si es valido")
else:
    print("El correo no es valido")
