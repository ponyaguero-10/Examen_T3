# Definir una clase para representar a un estudiante
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"


# Clase para gestionar el registro de estudiantes
class GestionEstudiantes:
    def __init__(self):
        self.estudiantes = []

    # Agregar un estudiante
    def agregar_estudiante(self, nombre, edad, carrera):
        estudiante = Estudiante(nombre, edad, carrera)
        self.estudiantes.append(estudiante)
        print(f"Estudiante {nombre} agregado correctamente.")

    # Eliminar un estudiante por nombre
    def eliminar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                self.estudiantes.remove(estudiante)
                print(f"Estudiante {nombre} eliminado correctamente.")
                return
        print(f"Estudiante {nombre} no encontrado.")

    # Mostrar todos los estudiantes
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("Lista de Estudiantes:")
            for estudiante in self.estudiantes:
                print(estudiante)

    # Buscar un estudiante por nombre
    def buscar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                print(f"Estudiante encontrado: {estudiante}")
                return
        print(f"Estudiante {nombre} no encontrado.")


# Función principal para interactuar con el sistema
def menu():
    gestion = GestionEstudiantes()

    while True:
        print("\n-- Menú de Gestión de Estudiantes --")
        print("1. Agregar Estudiante")
        print("2. Eliminar Estudiante")
        print("3. Mostrar todos los Estudiantes")
        print("4. Buscar Estudiante")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            carrera = input("Ingrese la carrera del estudiante: ")
            gestion.agregar_estudiante(nombre, edad, carrera)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del estudiante a eliminar: ")
            gestion.eliminar_estudiante(nombre)
        elif opcion == '3':
            gestion.mostrar_estudiantes()
        elif opcion == '4':
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            gestion.buscar_estudiante(nombre)
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
