#solicita un texto y suma todos los caracteres que no sean letras
#h03h7
texto=input("Ingrese un texto:")
contador=0
for i in texto:
    if i!='a' and i!='b' and i!='c' and i!='d' and i!='e' and i!='f' and i!='g' and i!='h' and i!='i' and i!='j' and i!='k' and i!='l' and i!='m' and i!='n' and i!='o' and i!='p' and i!='q' and i!='r' and i!='s' and i!='t' and i!='u' and i!='v' and i!='w' and i!='x' and i!='y' and i!='z':
        contador+=ord(i)
        print(ord(i))
print(f"EL texto {texto} su suma sin sus letras es:{contador}")