#texto_largo=xpnrrenorsrtoo
#texto_corto=perro
#abcd
#be
index=0
flag=False
texto_corto=input("Escribe una palabra (ejemplo=perro):")
texto_largo =input("Escribe un texto (ejemplo=xpnrrenorsrtoo):")
contador=len(texto_corto)
print(contador)
for a in texto_largo:
    if contador>0 and a == texto_corto[index]:
        print(a)
        index+=1
        contador-=1
    if contador==0:
        flag=True
if flag:
    print("La plabara si se puede formar")
else:
    print("La palabra no se puedo formar")