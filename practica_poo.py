class Datos_personales:
    def __init__(self):
        self.nombre = "None"
        self.apellido = "None"
        self.edad = 0
        self.cedula = "None"
        self.nacionalidad = "None"
        
    def ingresar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.edad = int(input("Ingrese su edad: "))
        self.cedula = input("Ingrese su cédula: ")
        self.nacionalidad = input("Ingrese su nacionalidad: ")
        
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Edad:", self.edad)
        print("Cédula:", self.cedula)
        print("Nacionalidad:", self.nacionalidad)
        
    def presentacion(self):
        print(f"Mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} anios, mi cédula de identidad es {self.cedula} y mi nacionalidad es {self.nacionalidad}.")
        
class Parientes(Datos_personales):
    def __init__(self):
        super().__init__()
        self.pariente = "None"
    
    def ingresar_datos_pariente(self):
        self.pariente = input("Ingrese el nombre de quien es pariente: ")
        super().ingresar_datos()
    
    def mostrar_datos_pariente(self):
        print("Pariente:", self.pariente)
        return super().mostrar_datos()
        
    def presentacion_pariente(self):
        print(f"Mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} anios, mi cédula de identidad es {self.cedula} y mi nacionalidad es {self.nacionalidad} y mi pariente es {self.pariente}.")
        return super().presentacion()
        
        
mis_datos = Datos_personales()
mis_datos_parientes = Parientes()
mis_datos_parientes.ingresar_datos_pariente()
mis_datos_parientes.mostrar_datos_pariente()
mis_datos_parientes.presentacion_pariente()

