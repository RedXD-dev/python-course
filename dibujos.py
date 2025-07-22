#tener 5 opciones en donde cada opcion va a enseñar una forma ejemplo 1 = triangulo, 2 = cuardado
def regresa_cuadrado():
    matriz_cuadrado = [
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
    ]

    return matriz_cuadrado
def regresa_triangulo():
    matriz_triangulo = [
        ["⬜","⬜","⬜","⬛","⬜","⬜","⬜"],
        ["⬜","⬜","⬛","⬜","⬛","⬜","⬜"],
        ["⬜","⬜","⬛","⬜","⬛","⬜","⬜"],
        ["⬜","⬛","⬜","⬜","⬜","⬛","⬜"],
        ["⬜","⬛","⬜","⬜","⬜","⬛","⬜"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
    ]

    return matriz_triangulo
def regresa_circulo():
    matriz_circulo = [
        ["⬜","⬜","⬛","⬛","⬛","⬜","⬜"],
        ["⬜","⬛","⬜","⬜","⬜","⬛","⬜"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬜","⬛","⬜","⬜","⬜","⬛","⬜"],
        ["⬜","⬜","⬛","⬛","⬛","⬜","⬜"]

    ]

    return matriz_circulo
def regresa_rectangulo():
    matriz_rectangulo = [
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
        
    ]
    return matriz_rectangulo
def regresa_trapecio():
    matriz_trapecio = [
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬛","⬜","⬜","⬜","⬜","⬜","⬛"],
        ["⬜","⬛","⬜","⬜","⬜","⬛","⬜"],
        ["⬜","⬛","⬜","⬜","⬜","⬛","⬜"],
        ["⬜","⬛","⬜","⬜","⬜","⬛","⬜"],
        ["⬜","⬛","⬜","⬜","⬜","⬛","⬜"],
        ["⬜","⬜","⬛","⬛","⬛","⬜","⬜"]
    ]
    return matriz_trapecio



def dibuja_matriz(matriz):
    filas = len(matriz)
    for i in range(0,filas):
        print(matriz[i])    






matriz_original = []
cosa=0
while cosa!=-1:
    figura=input("Ingrese '1' = cuadrado o '2' = triangulo o '3' = circulo o '4' = rectangulo o '5' = trapecio o 'fin' = terminar: ")
    if figura == 'fin':
        print('Gracias')
        cosa=-1
    else:
        if figura == '1':
            matriz_original = regresa_cuadrado()
            dibuja_matriz(matriz_original)

        elif figura == '2':
            matriz_original = regresa_triangulo()
            dibuja_matriz(matriz_original)
            
        elif figura == '3':
            matriz_original = regresa_circulo()
            dibuja_matriz(matriz_original)
            
        elif figura == '4':
            matriz_original = regresa_rectangulo()
            dibuja_matriz(matriz_original)

        elif figura == '5':
            matriz_original = regresa_trapecio()
            dibuja_matriz(matriz_original)
            
        else:
            print("Palabra o numero no valido, intentelo de nuevo")