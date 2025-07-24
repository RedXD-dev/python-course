class Iron_Man:
    def __init__(self,nombre,altura,año):
        self.nombre = nombre
        self.altura = altura
        self.año = año

    def volar(self):
        print(f"{self.nombre} esta volando")
    def disparar(self):
        print(f"{self.nombre} esta disparando")
    def inteligencia(self):
        print(f"{self.nombre} esta pensando y creando una estrategia")
nombre_1="Iron Man"
altura_1=1.85
año_1="Marzo de 1963"
personaje=Iron_Man(nombre_1,altura_1,año_1)
cosa=0
while cosa!=-1:
    menu=int(input("Ingrese '1' = datos o '2' = volar o '3' = disparar o '4' inteligencia o '5' = salir: "))
    if menu==5:
        print("Gracias")
        cosa=-1
    else:
        if menu==1:
            print(f"Nombre = {personaje.nombre}, Altura = {personaje.altura}, Año de creacion = {personaje.año}")
        elif menu==2:
            personaje.volar()
        elif menu==3:
            personaje.disparar()
        elif menu==4:
            personaje.inteligencia()