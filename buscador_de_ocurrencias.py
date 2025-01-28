#texto1=abcthgangtopqat
#texto2=gato
flag=False
contador=0
lista=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lista1=[]
texto1=input("Ingrese un texto (ejemplo 'gato'):")
for a in texto1:
    cosa=ord(a)-ord("a")
    lista[cosa]+=2
texto2=input("Ingrese un texto (ejemplo 'abcthgangtopqat')")
for e in texto2:
    cosa1=ord(e)-ord("a")
    lista[cosa1]-=1
for i in lista:
    if lista[contador]>0:
        flag=True
    contador+=1
if flag:
    print("La palabra no se puede repetir 2 veces")
else:
    print("La palabra se puede repetir 2 veces")
print(lista)
#Este es un cambio