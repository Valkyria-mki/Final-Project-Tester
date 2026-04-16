#Sistema de gesión básico
productos = []
while True:
    print("================================")
    print("=====Sistema Gestion Basico=====")
    print("================================\n")
    print("1. Agregar Producto")
    print("2. Mostrar Producto")
    print("3. Buscar Producto")
    print("4. Eliminar Producto")
    print("5. Salir\n")
    print("================================")


    opcion = input("\nElige una opcion(1-5): ").strip()
  
 
    if opcion == "1":
        print("\n ° Agregar producto ° \n")
              
        nombre= input("\nIngresa el nuevo producto: \n").strip()
        while nombre == "":
            print("\nError. El campo no puede estar vacío.\n")
            nombre= input("\nIngresa el nuevo producto: \n").strip()


        categoria= input("\nIngresa la categoria del producto: \n").strip()
        while categoria == "":
            print("\nError. El campo no puede estar vacío.\n")
            categoria= input("\nIngresa la categoria del producto: \n").strip() 


        while True:
         precio_str = input("\nIngresa el precio en numeros (sin centavos): \n").strip()
         if precio_str.isdigit():
            precio = int(precio_str)
            if precio > 0:
                break
            else:
                print("\nError. El precio debe ser un numero positivo.\n")
        else:
            print("Error. El precio debe ser un numero")

       
        producto_a_agregar = [nombre, categoria, precio]
        productos.append(producto_a_agregar)
        print(f"\nProducto '{nombre}' agregado exitosamente.\n")

    elif opcion == "2":
        print("\nLista Productos\n")
        print("\n*Nro     * Nombre * Categoria * Precio *\n")
        for item in range(len(productos)):
            p= productos[item]
            print(f"* {  item +1  }      * {p[0]}   *  {p[1]}     * {p[2]} * ")

    elif opcion == "3":
        print("\n ° Buscar producto ° \n")
        busqueda = input("\nIngresa el nombre del producto a buscar: \n").strip()
        
        encontrado = False
        for p in productos:
            if p[0].lower() == busqueda.lower():
                print("\n¡Producto encontrado!\n")
                print(f"Nombre: {p[0]}")
                print(f"Categoría: {p[1]}")
                print(f"Precio: {p[2]}")
                encontrado = True
                break
        
        if not encontrado:
            print("\nProducto no encontrado.\n")

    elif opcion == "4":
        print("\n ° Eliminar producto ° \n")
        if not productos:
            print("\nNo hay productos para eliminar.\n")
            continue
        
        producto_a_eliminar = input("\nIngresa el nombre del producto a eliminar: \n").strip()
        encontrado = False
  
        for i in range(len(productos)):
            if productos[i][0].lower() == producto_a_eliminar.lower():
                confirmacion = input(f"\n¿Estás seguro de que quieres eliminar '{productos[i][0]}'? (si/no): \n").strip().lower()
                if confirmacion == "si":
                    del productos[i]
                    print(f"\nProducto '{producto_a_eliminar}' eliminado exitosamente.\n")
                else:
                    print(f"\nEliminación de '{producto_a_eliminar}' cancelada.\n")
                encontrado = True
                break
        
        if not encontrado:
            print("\nProducto no encontrado.\n")     
            
    elif opcion == "5":
        print("Fin de Programa")
        break

    else:
        print("\nOpción no válida. Elige una opción del 1 al 5.\n")    


          

 
