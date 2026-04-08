class Venta:
    def __init__(self):
        with open("ventas.txt", "a+") as ventas:
            self.producto = ventas.readlines()
        self.id_producto = None
        self.nombre_producto = None
        self.cantidad = None
        self.precio = 0
        
    def agregar_producto(self):
            # Primero crear el archivo si no existe
        with open("ventas.txt", "a") as ventas:
            self.id_producto = int(input("ID del producto: "))
            self.nombre_producto = input("Nombre del producto: ")
            self.cantidad = int(input("Cantidad: "))
            self.precio = float(input("Precio: "))
            ventas.write(f"ID: {self.id_producto}\n Nombre: {self.nombre_producto}\n Cantidad: {self.cantidad}\n Precio: {self.precio}\n")
                
    def mostrar_productos(self):
        with open("ventas.txt", "r") as ventas:
            for linea in ventas:
                print(linea.strip())
                
    def comprar_producto(self):
    # Recargar productos del archivo
        with open("ventas.txt", "r") as ventas:
            self.producto = ventas.readlines()
    
            self.id_producto = int(input("ID del producto a comprar: "))
    
    # Buscar ID en líneas del archivo
        for i, linea in enumerate(self.producto):
            if f"ID: {self.id_producto}" in linea:
            # Extraer nombre y cantidad de líneas siguientes
                nombre_linea = self.producto[i+1].strip()
                cantidad_linea = self.producto[i+2].strip()
                self.nombre_producto = nombre_linea.replace("Nombre: ", "")
                self.cantidad = int(cantidad_linea.replace("Cantidad: ", ""))
            
            print(f"Producto Encontrado: {self.nombre_producto} - Precio: {self.precio}")
            cantidad_comprar = int(input("Cantidad a comprar: "))
            
            if cantidad_comprar <= self.cantidad:
                self.cantidad -= cantidad_comprar
                # Reescribir archivo actualizado
                self.producto[i+2] = f"Cantidad: {self.cantidad}\n"
                with open("ventas.txt", "w") as ventas:
                    ventas.writelines(self.producto)
                print(f"Compra realizada. Cantidad restante: {self.cantidad}")
                return
            else:
                print("No hay suficiente stock.")
                return
    
    print("Producto no encontrado.")

venta = Venta()

while True:
    opcion = input("Menú de venta:\n1. Agregar Producto.\n2. Mostrar Productos.\n3. Comprar Producto.\n4. Salir. \nIngrese una opcion: ")
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