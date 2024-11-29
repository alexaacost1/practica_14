def menu_maquillaje():
    lista_maquillaje = []
    while True:
        print("\nHecho por Alexa Y Dulce")
        print("\nMenú de Opciones - Gestión de Productos de Maquillaje")
        print("1) Agregar un Producto")
        print("2) Consultar Productos")
        print("3) Modificar un Producto")
        print("4) Eliminar un Producto")
        print("5) Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            # Agregar producto
            print("\nIngrese los datos del producto:")
            nombre = input("Nombre: ")
            marca = input("Marca: ")
            tipo = input("Tipo (ejemplo: base, sombra, labial): ")
            tonalidad = input("Tonalidad: ")
            tamanio = input("Tamaño (ml o g): ")
            precio = input("Precio: ")
            stock = input("Stock disponible: ")
            
            producto = {
                "Nombre": nombre,
                "Marca": marca,
                "Tipo": tipo,
                "Tonalidad": tonalidad,
                "Tamaño": tamanio,
                "Precio": precio,
                "Stock": stock
            }
            lista_maquillaje.append(producto)
            print("Producto agregado con éxito.")
        
        elif opcion == 2:
            # Consultar productos
            if not lista_maquillaje:
                print("No hay productos registrados.")
            else:
                print("\nListado de Productos:")
                for idx, producto in enumerate(lista_maquillaje, 1):
                    print(f"{idx}) {producto}")
        
        elif opcion == 3:
            # Modificar producto
            if not lista_maquillaje:
                print("No hay productos registrados.")
            else:
                print("\nListado de Productos:")
                for idx, producto in enumerate(lista_maquillaje, 1):
                    print(f"{idx}) {producto}")
                
                posicion = int(input("Ingrese el número del producto que desea modificar: "))
                if 1 <= posicion <= len(lista_maquillaje):
                    print("\nIngrese los nuevos datos del producto:")
                    nombre = input("Nombre: ")
                    marca = input("Marca: ")
                    tipo = input("Tipo (ejemplo: base, sombra, labial): ")
                    tonalidad = input("Tonalidad: ")
                    tamanio = input("Tamaño (ml o g): ")
                    precio = input("Precio: ")
                    stock = input("Stock disponible: ")
                    
                    lista_maquillaje[posicion - 1] = {
                        "Nombre": nombre,
                        "Marca": marca,
                        "Tipo": tipo,
                        "Tonalidad": tonalidad,
                        "Tamaño": tamanio,
                        "Precio": precio,
                        "Stock": stock
                    }
                    print("Producto modificado con éxito.")
                else:
                    print("Número de producto inválido.")
        
        elif opcion == 4:
            # Eliminar producto
            if not lista_maquillaje:
                print("No hay productos registrados.")
            else:
                print("\nListado de Productos:")
                for idx, producto in enumerate(lista_maquillaje, 1):
                    print(f"{idx}) {producto}")
                
                posicion = int(input("Ingrese el número del producto que desea eliminar: "))
                if 1 <= posicion <= len(lista_maquillaje):
                    lista_maquillaje.pop(posicion - 1)
                    print("Producto eliminado con éxito.")
                else:
                    print("Número de producto inválido.")
        
        elif opcion == 5:
            # Salir
            print("Saliendo del programa. ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu_maquillaje()
