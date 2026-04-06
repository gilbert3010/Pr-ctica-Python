class Venta:
    def __init__(self):
        self.producto = []
        self.nombre_producto = None
        self.cantidad = None
        self.precio = 0
        
    def agregar_producto(self):
            # Primero crear el archivo si no existe
        with open("ventas.txt", "a") as ventas:
            self.nombre_producto = input("Nombre del producto: ")
            self.cantidad = int(input("Cantidad: "))
            self.precio = float(input("Precio: "))
            ventas.write(f"Nombre: {self.nombre_producto}\n Cantidad: {self.cantidad}\n Precio: {self.precio}\n")
                
    def mostrar_productos(self):
        with open("ventas.txt", "r") as ventas:
            for linea in ventas:
                print(linea.strip())
                
    """"def comprar_producto(self, cantidad):
        with open("ventas.txt", "r") as ventas:
            print("Elige el producto que desea comprar: ")
            for i, self.nombre_producto in enumerate(ventas.readlines()):
                print(f"{i+1}. {self.nombre_producto}")
            
                if cantidad > self.cantidad:
                    print("Sobre límite de productos disponibles.")
                elif cantidad <= self.cantidad:
                    self.cantidad -= cantidad
                    print(f"Compra realizada. Quedan {self.cantidad} de {self.nombre_producto}productos dispobibles.")
                else:
                    print("Cantidad no válida.")"""
        
            
venta = Venta()

while True:
    opcion = input("Menú de venta:\n1. Agregar Producto.\n2.Mostrar Productos.\n3. Salir.\nOpción...: ")
    if opcion == "1":
        venta.agregar_producto()
    elif opcion == "2":
        venta.mostrar_productos()
    elif opcion == "3":
        print("Saliendo...")
        break
    else: print("Opción inválida.")