#vrt76e4rtv3678d4btrd764drq36
contador=0
texto=input("ingrese un texto alfa numerico (ejemplo=dearh3w283429):")
for i in texto:
    if i== '1' or i == '2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
        contador+=ord(i)-ord("0")

print(f"La suma del texto {texto} en alfa numerico su suma es:{contador}")