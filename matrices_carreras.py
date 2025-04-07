matris=[
    ["♟","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"]
]
fila = 0
columna = 0
cosa=""
while cosa != "fin":
    print(matris [0])
    print(matris [1])
    print(matris [2])
    print(matris [3])
    print(matris [4])
    matris=[
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"]
    ]
    print(fila,columna)
    cosa=input("Ingrese 'l' = ⬅ o 'u' = ⬆ o 'b' = ⬇  o 'r' = ⮕ o ingrese 'fin' para terminar: ")
    if cosa == "l":
        if columna!=0:
            columna-=1
        else:
            print("por aqui no se puuede pasar")
    elif cosa == "u":
        if fila!=0:
            fila-=1
        else:
            print("por aqui no se puuede pasar")
    elif cosa == "b":
        if fila!=5:
            fila+=1
        else:
            print("por aqui no se puuede pasar")
    elif cosa == "r":
        if columna!=5:
            columna+=1
        else:
            print("por aqui no se puuede pasar")
    matris[fila] [columna] = "♟"