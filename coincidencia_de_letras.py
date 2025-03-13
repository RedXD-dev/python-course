#Solicita al usuario un texto 
#y despues solicita letras hasta que coloque "Ñ"
#Imprime verdadero falso si las letras esatan contenidas en el texto
#Ejemplo:texto=perrogato
#letras=a,a,a,a,a,a,a,a,a,a,a,o
#resultado=perrogato si contiene la letras
texto=input("Ingrese un texto:")
texto2=""
flag=True
lista=[]
lista2=[]
contador=0
while texto2!= "°":
    texto2=input("Ingrese una palabra (o escribe '°' para terminar:)")
    lista.append(texto2)
lista.remove("°")
for a in lista:
    for e in texto:
       
       if a==e and contador==0:
           lista2.append(e)
           contador+=1
    contador=0
print(lista)
print(lista2)
if lista==lista2:
    print("",end="")
else:
    flag=False
    
           
if flag:
    print(f"{texto} si contiene las letras")
else:
    print(f"{texto} no contiene las letras")