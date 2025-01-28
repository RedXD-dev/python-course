#01/06/25  -> primero de junio del dos mil veinticico
mes=""
dia=""
listames=[]
listadia=[]
number=(input("ingrese una fecha (ejemplo:01/06/25):"))
lista=[]
a=number[0] + number[1]
b=number[3] + number [4]
if a=='01':
    dia="Primero"
elif a=='02':
    dia="Dos"
elif a=='03':
    dia="Tres"
elif a=='04':
    dia="Cuatro"
elif a=='05':
    dia="Cinco"
elif a=='06':
    dia="Seis"
elif a=='07':
    dia="Siete"
elif a=='08':
    dia="Ocho"
elif a=='09':
    dia="Nueve"
elif a=='10':
    dia="Diez"
elif a=='11':
    dia="Once"
elif a=='12':
    dia="Doce"
elif a=='13':
    dia="Trece"
elif a=='14':
    dia="Catorce"
elif a=='15':
    dia="Quince"
elif a=='16':
    dia="Diesiseis"
elif a=='17':
    dia="Diesisiete"
elif a=='18':
    dia="Diesiocho"
elif a=='19':
    dia="Diesinueve"
elif a=='20':
    dia="Veinte"
elif a=='21':
    dia="Veintiuno"
elif a=='22':
    dia="Veintidos"
elif a=='23':
    dia="Veintitres"
elif a=='24':
    dia="Veinticuatro"
elif a=='25':
    dia="Veinticinco"
elif a=='26':
    dia="Veintiseis"
elif a=='27':
    dia="Veintisiete"
elif a=='28':
    dia="Veintiocho"
elif a=='29':
    dia="Veintinueve"
elif a=='30':
    dia="Treinta"
elif a=='31':
    dia="Treinta y uno"



if b=='01':
    mes="Enero"
elif b=='02':
    mes="Febrero"
elif b=='03':
    mes="Marzo"
elif b=='04':
    mes="Abril"
elif b=='05':
    mes="Mayo"
elif b=='06':
    mes="Junio"
elif b=='07':
    mes="Julio"
elif b=='08':
    mes="Agosto"
elif b=='09':
    mes="Septiembre"
elif b=='10':
    mes="Octubre"
elif b=='11':
    mes="Noviembre"
elif b=='12':
    mes="Diciembre"
print(f"El {number} escrito es: {dia} de {mes} del dos mil veinticinco")