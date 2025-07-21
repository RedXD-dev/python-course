#print("hola")

"""def saludar(): { 
    print("hola")
}"""
#Una funcion comenza con def y despues es el nombre de la funcion 
#despues los parentesis y al final llaves
#saludar()
#Entre los parentisis podemos recibir parametros 
#def sumar(num1,num2): {
#    print(num1+num2)
#}
#sumar(10,10)
#def division(num1,num2): 
#    return num1/num2
#
#resultado= division(10,5)
#print(resultado)
#cosa1=int(input())
#cosa2=int(input())
"""def multiplicar(num1,num2):
    return num1*num2
resultado= multiplicar(cosa1,cosa2)
print(resultado)"""
"""cosa1=int(input())
cosa2=int(input())
cosa3=int(input())
cosa4=int(input())
cosa5=int(input())
def numeros(num1,num2,num3,num4,num5):
    return num1+num2-num3*num4/num5
resultado = numeros(cosa1,cosa2,cosa3,cosa4,cosa5)
print(resultado)"""
cosa1=int(input())
cosa2=int(input())

def matris(fila,columna):
    
    flag_fila=fila>=0 and fila<=2
    flag_columna=columna>=0 and columna<=2
    return flag_fila and flag_columna
resultado= matris(cosa1,cosa2)

print(resultado)