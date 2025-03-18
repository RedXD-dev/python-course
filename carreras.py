#Solicta al usuario una longitud
#Cada vez que el usuario escriba "b" retrocedera un espacio
#Cada vez que coloque "f" Se movera hacia adelante
#Ejemplo:Longitud=10
#🚗__________
#el usuario ingresa f
#_🚗_________
#Imprime=0
contador=-1
carrito=0
Longitud=input("Ingrese la longitud de la pista: ")
lista=["🚗"]
for a in range(int(Longitud)):
    lista.append("_")
while carrito < int(Longitud):
    for e in lista:
        print(carrito)
        print(lista)
        print(Longitud)
        cosa=input("Ingrese 'f' para moverse hacia delante y 'b' para retroceder: ")
        if cosa=="f":
            carrito+=1
            lista.insert(0,"_")
            lista.pop()
        elif cosa=="b":
            if carrito>=1:
                carrito-=1
                lista.pop(0)
                lista.append("_")
            else:
                print("Tu carrito no puede retroceder")
                contador-=1
        contador+=1
print(f"Tu 🚗 le tomo {contador} intentos en llegar al final")