#Solicita al usuario una cifra e imrpime sus digitos alrevez sin usar texto
numero=int(input("Ingrese un numero: "))
while numero!=0:
    ultimo_digito=numero%10
    numero= int(numero/10)
    print(ultimo_digito,end="")
print()