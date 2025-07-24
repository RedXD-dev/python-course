class Iron_Man:
    def __init__(self,nombre,altura,año,nivel_vida):
        self.nombre = nombre
        self.altura = altura
        self.año = año
        self.nivel_vida = nivel_vida

    def volar(self):
        print(f"{self.nombre} esta volando")
    def disparar(self):
        print(f"{self.nombre} esta disparando")
    def inteligencia(self):
        print(f"{self.nombre} esta pensando y creando una estrategia")
    def recibir_daño(self):
        self.nivel_vida-=1
        print(f"{self.nombre} recibio daño")

        
nombre_1="Iron Man"
altura_1=1.85
año_1="Marzo de 1963"
vida=10
personaje=Iron_Man(nombre_1,altura_1,año_1,vida)
cosa=0
while cosa!=-1:
    menu=int(input("Ingrese '1' = datos o '2' = volar o '3' = disparar o '4' inteligencia o '5' = recibir daño o '6' mostrar vida o '7' = salir: "))
    if menu==7:
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
        elif menu==5:
            personaje.recibir_daño()
        elif menu==6:
            print(f"{personaje.nombre} tiene {personaje.nivel_vida} de vida")