import random

class GeneradorPalabras:
    def generar_palabra(self):
        palabra = ""
        for i in range(4):
            letra = chr(random.randint(97, 122))
            palabra += letra
        return palabra

class MatrizPalabras:
    def __init__(self, tamano):
        self.tamano = tamano
        self.matriz = []
        self.generador = GeneradorPalabras()
    
    def crear(self):
        for i in range(self.tamano):
            fila = []
            for j in range(self.tamano):
                fila.append(self.generador.generar_palabra())
            self.matriz.append(fila)
    
    def mostrar(self):
        print("\nMatriz de palabras generada:")
        print("-" * (self.tamano * 6))
        for fila in self.matriz:
            linea = ""
            for palabra in fila:
                linea += palabra + "  "
            print(linea)
        print("-" * (self.tamano * 6))
    
    def obtener_matriz(self):
        return self.matriz

class AnalizadorVocales:
    def __init__(self):
        self.vocales = "aeiou"
    
    def tiene_vocal(self, palabra):
        for letra in palabra:
            if letra in self.vocales:
                return True
        return False

class ContadorDivideYVenceras:
    def __init__(self, matriz):
        self.matriz = matriz
        self.analizador = AnalizadorVocales()
    
    def contar(self, fila_inicio, fila_fin, columna_inicio, columna_fin):
        if fila_inicio == fila_fin and columna_inicio == columna_fin:
            palabra = self.matriz[fila_inicio][columna_inicio]
            if self.analizador.tiene_vocal(palabra):
                return 1
            else:
                return 0
        
        if fila_inicio == fila_fin:
            columna_mitad = (columna_inicio + columna_fin) // 2
            izquierda = self.contar(fila_inicio, fila_fin, columna_inicio, columna_mitad)
            derecha = self.contar(fila_inicio, fila_fin, columna_mitad + 1, columna_fin)
            return izquierda + derecha
        
        if columna_inicio == columna_fin:
            fila_mitad = (fila_inicio + fila_fin) // 2
            arriba = self.contar(fila_inicio, fila_mitad, columna_inicio, columna_fin)
            abajo = self.contar(fila_mitad + 1, fila_fin, columna_inicio, columna_fin)
            return arriba + abajo
        
        fila_mitad = (fila_inicio + fila_fin) // 2
        columna_mitad = (columna_inicio + columna_fin) // 2
        
        superior_izquierda = self.contar(fila_inicio, fila_mitad, columna_inicio, columna_mitad)
        superior_derecha = self.contar(fila_inicio, fila_mitad, columna_mitad + 1, columna_fin)
        inferior_izquierda = self.contar(fila_mitad + 1, fila_fin, columna_inicio, columna_mitad)
        inferior_derecha = self.contar(fila_mitad + 1, fila_fin, columna_mitad + 1, columna_fin)
        
        return superior_izquierda + superior_derecha + inferior_izquierda + inferior_derecha

class Aplicacion:
    def ejecutar(self):
        print("=" * 50)
        print("CONTADOR DE PALABRAS CON VOCALES")
        print("Algoritmo: Divide y Venceras")
        print("=" * 50)
        
        tamano = int(input("\nIngrese el tamano de la matriz cuadrada: "))
        
        matriz_palabras = MatrizPalabras(tamano)
        matriz_palabras.crear()
        matriz_palabras.mostrar()
        
        contador = ContadorDivideYVenceras(matriz_palabras.obtener_matriz())
        total_palabras_con_vocales = contador.contar(0, tamano - 1, 0, tamano - 1)
        
        print(f"\nResultado:")
        print(f"Palabras con al menos una vocal: {total_palabras_con_vocales}")
        print(f"Total de palabras en la matriz: {tamano * tamano}")
        print("=" * 50)

if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.ejecutar()