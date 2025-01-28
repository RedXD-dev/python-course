#01-------05----25
lista=[]
fecha=input("ingrese una fecha (ejemplo:01-------05----25):")
for i in fecha:
    if i=="0":
        lista.append(i)
    elif i=="1":
        lista.append(i)
    elif i=="2":
        lista.append(i)
    elif i=="3":
        lista.append(i)
    elif i=="4":
        lista.append(i)
    elif i=="5":
        lista.append(i)
    elif i=="6":
        lista.append(i)
    elif i=="7":
        lista.append(i)
    elif i=="8":
        lista.append(i)
    elif i=="9":
        lista.append(i)
lista.insert(2,"-")
lista.insert(5,"-")
for caracter in lista:
    print(caracter,end="")
print()
