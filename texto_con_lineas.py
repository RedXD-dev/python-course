#texto=hola
#print(h-o-l-a)
texto=input("Ingrese un texto: ")
contador=len(texto)-1
lista=[]

for a in texto:
    lista.append(a)
    if contador!=0:
        lista.append("-")
    contador-=1
for e in lista:
    print(e,end="")
#h-o-l-a