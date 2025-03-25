lista=[]
flag=True
cosa=0
contador=0
while cosa!=-1:
    cosa=int(input("Ingresa un numero (o escribe '-1' para terminar):"))
    lista.append(cosa)
lista.remove(-1)
for a in lista:
    if contador < a:
        print(contador)
        contador=a
        print(a)
    elif contador> a:
        flag=False
print(flag)
if flag:
    print("La lista esta de manera ascendente")
else:
    print("La lista no esta de manera ascendente")