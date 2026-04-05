class Personaje:
    def __init__(self, nombre = None, vida = 100, ataque = 10, defensa = 5):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        
    def ingresar_nombre(self):
        self.nombre = input(f"Ingrese el nombre de su personaje: ")
        
    def mostrar_atributos(self, nombre, vida, ataque, defensa):
        print(f"Nombre: {nombre}")
        print(f"Vida: {vida}")
        print(f"Ataque: {ataque}")
        print(f"Defensa: {defensa}")
    
class Guerrero(Personaje):
    def __init__(self, nombre=None, vida=100, ataque=10, defensa=5, arma="30", armadura="20"):
        super().__init__(nombre, vida, ataque, defensa)
        self.arma = arma
        self.armadura = armadura
    def ingresar_nombre(self):
        self.nombre = input(f"Ingrese el nombre de su Guerrero: ")

    def atributos(self, arma, armadura):
        ataque_total = self.ataque + int(arma)
        defensa_total = self.defensa + int(armadura)
        super().mostrar_atributos(self.nombre, self.vida, self.ataque, self.defensa)
        print(f"Ataque total: {ataque_total}")
        print(f"Defensa total: {defensa_total}")
        
class Mago(Personaje):
    def __init__(self, nombre=None, vida=100, ataque=10, defensa=5, arma_magica="40", vestido_magico="10"):
        super().__init__(nombre, vida, ataque, defensa)
        self.arma_magica = arma_magica
        self.vestido_magico = vestido_magico
    
    def ingresar_nombre(self):
        self.nombre = input(f"Ingrese el nombre de su Mago: ")

    def atributos(self, arma_magica, vestido_magico):
        ataque_total = self.ataque + int(arma_magica)
        defensa_total = self.defensa + int(vestido_magico)
        super().mostrar_atributos(self.nombre, self.vida, self.ataque, self.defensa)
        print(f"Ataque total: {ataque_total}")
        print(f"Defensa total: {defensa_total}")
        

#mi_personaje = Personaje(Guerrero)

guerrero = Guerrero()
mago = Mago()

guerrero.ingresar_nombre()
guerrero.atributos(guerrero.arma, guerrero.armadura)
mago.ingresar_nombre()
mago.atributos(mago.arma_magica, mago.vestido_magico)
