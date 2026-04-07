class Venta:
    def __init__(self):
        with open("ventas.txt", "r") as ventas:
            self.producto = ventas.readlines()
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
                
    def comprar_producto(self):
        if self.producto and self.nombre_producto:
            with open("ventas.txt", "r") as ventas:
                lista_producto = ventas.readlines()
            print(input("Que producto desea comprar?: "))
            self.cantidad -= int(input("Ingrese la cantidad: "))
            lista_producto.close()
        else:
            print("Producto no disponible.")
            
            
venta = Venta()

while True:
    opcion = input("Menú de venta:\n1. Agregar Producto.\n2.Mostrar Productos.\n3. Comprar Producto.\n4.Salir. \nIngrese una opcion: ")
    if opcion == "1":
        venta.agregar_producto()
    elif opcion == "2":
        venta.mostrar_productos()
    elif opcion == "3":
        venta.comprar_producto()
    elif opcion == "4":
        print("Saliendo...")
        break
    else: print("Opción inválida.")