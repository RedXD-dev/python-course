#solicita al usuario dos textos
#Texto1=saosoxoo
#Texto2=oso
#retorna cuantas veces texto2 puede formarse con texto1
#o==2
#s==1
#o en el texto1 es igual 10
#s en el texto1 es igual 2
flag=False
contador2=0
contador=0
lista=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
texto=input("Ingrese una palabra (ejemplo=oso):")
for p in texto:
    contador=ord(p)-ord("a")
    lista[contador]+=1
palabra=input("Ingrese una palabra (ejemplo='saosoxoo'):")

for i in palabra:
    contador=ord(i)-ord("a")
    lista[contador]-=1

for m in lista:
    if m>0:
        flag=True

print(lista)

if flag:
    print("La palabra no se puede crear")
else:
    print("La palabra si se pudo crear")
    
