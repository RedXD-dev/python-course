#nombre@dominio.com
flag_name=False
flag_arroba=False
flag_dominio=False
flag_com=False
lista=[]
contador=0
contador_arroba=0
contador_posicion=1
contador2=0
contador_com=0
contador4=0
correo=input("Ingrese un correo: ")

for a in correo:
    lista.append(a)
    contador+=1
flag_name=lista[0]!="@"

if flag_name:
    for e in lista:
        contador2+=contador_posicion
        if e=="@":
            contador_posicion-=1
            contador_arroba+=1
    flag_arroba=contador_arroba==1
if flag_name and flag_arroba:
    for i in lista[contador2:contador]:
        if i==".":
            contador4+=1
    flag_dominio=lista[contador2]!="." and contador4==1

if flag_name and flag_arroba and flag_dominio:
    if lista[contador-4]==".":
        contador_com+=1
    if lista[contador-3]=="c":
        contador_com+=1
    if lista[contador-2]=="o":
        contador_com+=1
    if lista[contador-1]=="m":
        contador_com+=1
        
    flag_com=contador_com==4

if flag_name and flag_arroba and flag_dominio and flag_com:
    print("El correo si es valido")
else:
    print("El correo no es valido")