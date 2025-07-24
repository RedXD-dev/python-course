class Auto:
    def __init__(self , color , marca):
        self.color = color
        self.marca = marca

    def arrancar(self):
        print("arrancando")

    def frenar(self):
        print("frenando")

    def derecha(self):
        print("girar a la derecha")

    def izquierda(self):
        print("girar a la izquierda")

########################################################################################################################

color_auto=input("Ingrese de que color es su auto: ")
marca_auto=input("Ingrese de que marca es su auto: ")

auto_papa=Auto(color_auto , marca_auto)

color_auto1=input("Ingrese de que color es su auto: ")
marca_auto1=input("Ingrese de que marca es su auto: ")

auto_tio=Auto(color_auto1 , marca_auto1)

print(f"El color del auto de mi papa es {auto_papa.color} y la marca es {auto_papa.marca}")
auto_papa.arrancar()
auto_papa.derecha()
auto_papa.frenar()
print()
print(f"El color del auto de mi tio es {auto_tio.color} y la marca es {auto_tio.marca}")
auto_tio.arrancar()
auto_tio.izquierda()
auto_tio.derecha()
auto_tio.frenar()