#create a dictionary
tienda = {}

print("<-----BIENVENIDO A TU TIENDA QUE DESEAS REALIZAR-----> ")

#We define the functions of each option
def agregar():

    producto = input("\nagregue el nombre del producto: ")
    if producto in tienda:
         print("el producto ya esta en inventario ")
         return
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        if precio < 0 or cantidad < 0:
            print("El precio y la cantidad deben ser valores positivos.")
            return
        tienda[producto] = (precio, cantidad)
        print(f"\033[92mProducto '{producto}' añadido exitosamente.\033[0m")
    except ValueError:
        print("\033[91mError: Ingrese un valor numérico válido para precio y cantidad.\033[0m")
    
def consultar():
    nombre = input("ingrese el nombre del producto que deseas consultar: ")
    if nombre in tienda:
        precio,cantidad = tienda[nombre]
        print(f"\033[92mnombre: {nombre}, precio: {precio}, cantidad:{cantidad}\033[0m ")
    else:
         print("\033[91mel producto no esta en inventario\033[0m")

def actualizar():


    nom = input("ingresa el nombre del producto: ")
    if nom in tienda:
            try:
                precio_nuevo = float(input("ingrese el nuevo precio del producto:"))
                if precio_nuevo < 0:
                    print("El precio debe ser un valor positivo.")
                    return
                cantidad = tienda[nom][1] 
                tienda[nom] = (precio_nuevo, cantidad) 
                print(f"\033[92mprecio '{nom}'actualizado a ${precio_nuevo:.2f}\033[0m")
            except ValueError:
                 print("ingrese un valor numerico valido para el precio")
    else:
        print("\033[91mel producto no esta en inventario\033[0m")

def eliminar():
    nom = input("ingrese el nombre del producto que deseas eliminar: ")
    if nom in tienda:
        del tienda[nom]
        print(f"\033[91mproducto '{nom}' eliminado del inventario\033[0m")
    else:
        print("el producto no esta en inventario")

def calcular():
     calcular_valor = lambda precio, cantidad: precio * cantidad 
     operacion = sum(calcular_valor(precio, cantidad) for precio, cantidad in tienda.values())  
     print(f"\033[92mel valor total del inventario es: ${operacion:.2f}\033[0m") 

  

#we create menu and options 
while True:
    print("\n1) Añadir productos al inventario  \n2) Consultar productos en inventario " 
        "\n3) Actualizar precios de productos \n4) Eliminar productos del inventario \n5) Calcular el valor total del inventario" )
    opcion = int(input("ingresa una opcion del 1 al 5 : "))
    if opcion == 1:
            agregar()
    elif opcion == 2:
         consultar()
    elif opcion == 3:
         actualizar()
    elif opcion == 4:
         eliminar()
    elif opcion == 5:
         calcular()
         break
    else:
         print("\033[91mopcion invalidad\033[0m")   


