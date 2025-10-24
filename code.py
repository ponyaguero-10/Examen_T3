# 🛍️ Sistema de Tienda en Python

# Productos disponibles (nombre: precio)
productos = {
    "Arroz": 4.50,
    "Azúcar": 3.80,
    "Leche": 5.20,
    "Aceite": 7.90,
    "Pan": 1.00,
    "Huevos": 0.60
}

# Carrito del usuario
carrito = {}

def mostrar_productos():
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for producto, precio in productos.items():
        print(f"{producto} - S/ {precio:.2f}")
    print("-----------------------------")

def agregar_al_carrito():
    mostrar_productos()
    producto = input("Ingrese el nombre del producto que desea agregar: ").capitalize()
    if producto in productos:
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        if producto in carrito:
            carrito[producto] += cantidad
        else:
            carrito[producto] = cantidad
        print(f"✅ {cantidad} {producto}(s) agregado(s) al carrito.")
    else:
        print("❌ Producto no encontrado.")

def ver_carrito():
    if not carrito:
        print("\n🛒 Tu carrito está vacío.")
        return
    print("\n--- TU CARRITO ---")
    total = 0
    for producto, cantidad in carrito.items():
        subtotal = productos[producto] * cantidad
        total += subtotal
        print(f"{producto} x{cantidad} = S/ {subtotal:.2f}")
    print(f"TOTAL: S/ {total:.2f}")
    print("------------------")

def calcular_total():
    if not carrito:
        print("\n⚠️ No hay productos en el carrito.")
        return
    total = sum(productos[p] * c for p, c in carrito.items())
    print(f"\n💰 El total de tu compra es: S/ {total:.2f}")
    print("¡Gracias por tu compra! 🛍️")

def menu():
    while True:
        print("\n===== SISTEMA DE TIENDA =====")
        print("1. Ver productos")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_al_carrito()
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            calcular_total()
            carrito.clear()  # Vacía el carrito después de la compra
        elif opcion == "5":
            print("👋 Gracias por visitar la tienda. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

# Ejecución del programa
menu()
