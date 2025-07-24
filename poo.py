#Para crear una clase class nombre de la clase 
class Persona: 
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def caminar(self):
        print("caminando")

########################################

"""persona_1 = Persona("Juan" , 13)
print(persona_1.nombre)
print(persona_1.edad)

persona_1.caminar()


persona_2 = Persona("Pepe" , 15)
print(persona_2.nombre)
print(persona_2.edad) """

#capturar estudianes hasta que pongas -1
cosa=0
lista=[]
while cosa!=-1:
    persona_1=input("Ingrese un nombre del estudiante: ")
    edad_1=input("Ingrese una edad: ")
    alumno = Persona(persona_1 , edad_1)
    lista.append(alumno)
    numero=int(input("Escriba '-1' para terminar o escriba cualquier numero: "))
    if numero==-1:
        cosa=-1
for p in lista:
    print(p.nombre)
    print()
    print(p.edad)
    print()