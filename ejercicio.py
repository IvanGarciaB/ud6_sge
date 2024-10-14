import json
import os

if not os.path.exists("inventario.json") or os.path.getsize("inventario.json") == 0:
    productos = []
    with open("inventario.txt", "r") as fichero:
        lineas = fichero.readlines()
        for linea in lineas:
            nombre, precio, cantidad = linea.strip().split(",")
            diccionario = {"Nombre": nombre, "Precio": precio, "Cantidad": cantidad}
            productos.append(diccionario)


    with open("inventario.json", "w") as fichero:
        json.dump({"productos": productos}, fichero, indent=4)

def reponer_stock():
    with open("inventario.json", "r") as fichero:
        data = json.load(fichero)

    productos = data["productos"]
    print("¿Qué producto desea reponer?")
    for producto in productos:
        print(f"Producto: {producto['Nombre']}, Stock: {producto['Cantidad']}")

    reponer = input("Escriba el nombre exacto del producto: ")
    cantidad_r = int(input("¿Cuántos desea añadir al stock?: "))

    for producto in productos:
        if producto["Nombre"] == reponer:
            producto["Cantidad"] = str(int(producto["Cantidad"]) + cantidad_r)
            print(f"Se han añadido {cantidad_r} de {reponer}. Ahora hay {producto['Cantidad']} en stock.")
            with open("inventario.json", "w") as fichero:
                json.dump({"productos": productos}, fichero, indent=4)
                break
    else:
        print(f"Producto {reponer} no encontrado en el inventario.")



def ver_inventario():
    with open("inventario.json", "r") as fichero:
        data = json.load(fichero)
        productos = data["productos"]
        for producto in productos:
            nombre = producto["Nombre"]
            precio = producto["Precio"]
            cantidad = producto["Cantidad"]
            print(f"Producto: {nombre}, Precio: {precio}, Stock: {cantidad}")
            if cantidad == 0:
                print(f"No hay stock de {nombre}")

def ventas():
    with open("inventario.json", "r") as fichero:
        data = json.load(fichero)

    productos = data["productos"]
    print("¿Qué desea vender?")
    for producto in productos:
        print(f"Producto: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Cantidad']}")

    venta = input("Escriba el nombre exacto del producto: ")
    cantidad_v = input("¿Cuántos desea vender?: ")

    for producto in productos:
        if producto["Nombre"] == venta:
            if int(producto["Cantidad"]) >= int(cantidad_v):
                producto["Cantidad"] = str(int(producto["Cantidad"]) - int(cantidad_v))
                print(f"Se han vendido {cantidad_v} de {venta}. Quedan {producto['Cantidad']} en stock.")
            else:
                print(f"No hay suficiente stock de {venta}.")
            break
    else:
        print(f"Producto {venta} no encontrado en el inventario.")

    with open("inventario.json", "w") as fichero:
        json.dump({"productos": productos}, fichero, indent=4)

def anadir_producto():
    with open("inventario.json", "r") as fichero:
        data = json.load(fichero)

    productos = data["productos"]
    nombre = input("Nombre del producto: ")
    precio = input("Precio del producto: ")
    cantidad = input("Cantidad del producto: ")
    diccionario = {"Nombre": nombre, "Precio": precio, "Cantidad": cantidad}
    productos.append(diccionario)

    with open("inventario.json", "w") as fichero:
        json.dump({"productos": productos}, fichero, indent=4)
        print("Producto añadido correctamente al inventario.")

def eliminar_producto():


def menu():
    while True:
        print("1. Ver inventario")
        print("2. Hacer venta")
        print("3. Reponer producto")
        print("4. Añadir producto")
        print("5. Salir")
        opcion = int(input ("¿Que desea hacer?: "))

        if opcion == 1:
            ver_inventario()
        elif opcion == 2:
            ventas()
        elif opcion ==3:
            reponer_stock()
        elif opcion == 4:
            anadir_producto()
        else:
            exit()

menu()



