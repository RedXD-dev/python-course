numero=int(input("Ingresa un numero para definir el limite:"))
contador=0
lista=[]
for a in range(numero):
    contador+=2
    lista.append(contador)
print(f"n={contador} , Resultado:{lista}")