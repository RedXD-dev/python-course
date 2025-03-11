texto=input("Ingrese un texto alfanumerico:")
for a in texto:
    contador=ord(a)-ord("A")

    if contador==0 or contador==4 or contador==8 or contador==14 or contador==20:
        print("",end="")

    else:
        if contador>=0 and contador<=25:
            print(a,end="")

    if contador==32 or contador==36 or contador==40 or contador==46 or contador==52:
         print("",end="")
         
    else:
        if contador>=32 and contador<=57:
            print(a,end="")
print()