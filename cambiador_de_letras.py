#solicita al usuario un texto
#y cambia las letras en la posicion impar a una posicion par
#Ejemplo:abcd----badc
#letras_pares=a,c
#letras_impares=b,d
#texto=gato
#lista=[_,_,_,_]
lista=[]
lista_par=[]
lista_impar=[]
texto=input("Ingrese un texto:")
index=0
for a in texto:
    lista.append("_")
for b in texto:
    if index%2!=0:
        lista_impar.append(b)
    else:
        lista_par.append(b)
    index+=1
index=1
for c in lista_par:
    if index%2!=0:
        lista.pop(index)
        lista.insert(index,c)
    index+=2
index=0
for d in lista_impar:
    if index%2==0:
        lista.pop(index)
        lista.insert(index,d)
    index+=2
for e in lista: 
    print(e,end="")