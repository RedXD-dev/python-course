#Solicita al usuario ingresar dos listas de caracteres
#Lista1=1,2,3
#lista2=a,b,c,d,e
#resultado=3,2,1,e,d,c,b,a
texto=0
texto1=0
lista=[]
lista1=[]
contador=-2
contador1=-2
while texto!="-1":
    texto=input("Ingresa un caracter para la primera lista (o escribe '-1' para terminar:)")
    lista.append(texto)
    contador+=1

while texto1!="-1":
    texto1=input("Ingresa un caracter para la segunda lista (o escribe '-1' para terminar:)")
    lista1.append(texto1)
    contador1+=1
lista.remove("-1")
lista1.remove("-1")
for a in lista:
    print(lista[contador],end="")
    contador-=1
for e in lista1:
    print(lista1[contador1],end="")
    contador1-=1
print()