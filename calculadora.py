def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def division(num1,num2):
    return num1/num2

def multiplicacion(num1,num2):
    return num1*num2

def calculadora(): 
    number1=0
    number2=0
    cosa=0
    while cosa!=-1:
        simbolo=input("Escribe '+' para sumar o '-' para restar o '/' para dividir o '*' para multiplicar o 'fin' para terminar: ")
        if simbolo=="fin":
            print("gracias")
            cosa=-1
        else:
            if simbolo=="+":
                number1=int(input("escriba un numero: "))
                number2=int(input("escriba un numero: "))
                resultado_suma= suma(number1,number2)
                print(resultado_suma)
            elif simbolo=="-":
                number1=int(input("escriba un numero: "))
                number2=int(input("escriba un numero: "))
                resultado_resta= resta(number1,number2)
                print(resultado_resta)
            elif simbolo=="/":
                number1=int(input("escriba un numero: "))
                number2=int(input("escriba un numero: "))
                resultado_division= division(number1,number2)
                print(resultado_division)
            elif simbolo=="*":
                number1=int(input("escriba un numero: "))
                number2=int(input("escriba un numero: "))
                resultado_multiplicacion= multiplicacion(number1,number2)
                print(resultado_multiplicacion)
            else: 
                print("Error de simbolo escriba otro")


def llamar_una_funcion_dentro_de_otra():
    calculadora()
llamar_una_funcion_dentro_de_otra()