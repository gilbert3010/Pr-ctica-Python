class Personaje:
    def __init__(self, nombre = None, vida = 100, ataque = 10, defensa = 5):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        
    def ingresar_nombre(self):
        self.nombre = input("Ingrese el nombre de su personaje: ")
        
    def mostrar_atributos(self, nombre, vida, ataque, defensa):
        print(f"Nombre: {nombre}")
        print(f"Vida: {vida}")
        print(f"Ataque: {ataque}")
        print(f"Defensa: {defensa}")

mi_personaje = Personaje()
        
while True:
    opcion = input("Elija una opcion: \n1. Ingresar nombre de Personaje. \n2. Mostrar Atributos. \n3. Salir.")
    if opcion == "1":
        mi_personaje.ingresar_nombre()
    elif opcion == "2":
        mi_personaje.mostrar_atributos(mi_personaje.nombre, mi_personaje.vida, mi_personaje.ataque, mi_personaje.defensa)
    elif opcion == "3":
        print("Saliendo...")
        break
            