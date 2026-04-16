class Persona:
    nombre = "Hola"
    edad = 0
    pais_origen = ""
    
    def atributos_persona(self, nombre, edad, pais_origen):
        self.nombre = nombre
        self.edad = edad
        self.pais_origen = pais_origen
        
    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Pais de origen: {self.pais_origen}")

mi_persona = Persona()
mi_persona.atributos_persona("Gilberto", 22, "Venezuela")
mi_persona.mostrar_atributos()