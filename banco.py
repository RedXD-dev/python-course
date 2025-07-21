#Saldo inicial 700 el usuario puede realizar las siguientes funciones:
#abonar dinero, retirar numero, consultar dinero y no permitir riterar dinero si el saldo es insuficiente
def agregar(num1,num2):
   return num1+num2




def retirar (num1,num2):
    temp = num1 - num2
    resultado = 0
    if temp<0:
        print("Lo siento pero no puede retirar porque no cuenta con el dinero")
        resultado = num1
    elif resultado>=0:
        print(f"Se retiro {numero} pesos")
        resultado = temp
    
    return resultado













saldo=700
numero=0
saldo_2=0
cosa=0

while cosa!=-1:
    funcion=input("Escriba '+' para abonar dinero o '-' para retirar dinero o '=' para consultar su dinero o 'fin' para terminar: ")
    if funcion=="fin":
        print("Gracias")
        cosa=-1
    else:    
        if funcion=="+":
            numero=int(input("Ingrese cuanto dinero quiere abonar: "))
            saldo = agregar(saldo,numero)
            print(f"Se abono {numero} pesos ")
        elif funcion=="-":
            numero=int(input("Ingrese cuanto dinero quiere retirar: "))
            saldo = retirar(saldo,numero)
        elif funcion=="=":
            print(f"Actualmente tiene {saldo} pesos")
