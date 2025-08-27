palabra=input("Ingrese una palabra (ejemplo=gato):")
contador=len(palabra)
if contador %2==0:
    print(f"La palabra {palabra} es par por su longitud")
else:
    print(f"La palabra {palabra} es impar por su longitud")
print(contador)