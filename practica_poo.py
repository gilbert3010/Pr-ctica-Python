class Datos_personales:
    def __init__(self):
        self.nombre = "Non"
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
        
        
        
mis_datos = Datos_personales()
mis_datos_pariente = Parientes()

while True:
    opcion = input("Que opción desea tomar? \n1.ingresar Datos \n2. Mostrar Datos \n3. Presentación \n4.Ingresar Pariente  \n5.Mostrar Datos Acutalizado \n6. Presentacion Actualizada \n7. Salir \n8. Volver al menú.\n")
    if opcion == "1":
        mis_datos.ingresar_datos()
    elif opcion == "2":
        mis_datos.mostrar_datos()
    elif opcion == "3":
        mis_datos.presentacion()
    elif opcion == "4":
        mis_datos_pariente.ingresar_datos_pariente()
    elif opcion == "5":
        mis_datos_pariente.mostrar_datos_pariente()
    elif opcion == "6":
        mis_datos_pariente.presentacion_pariente()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    elif opcion == "8":
        continue
    else:
        print("Opción invalida.")

