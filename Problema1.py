import copy

def crear_laberinto():
    laberinto = [
        [1, 1, 1, 1, 99, 1, 1, 1, 1],
        [1, 99, 99, 1, 99, 1, 99, 1, 99],
        [1, 1, 99, 1, 1, 1, 99, 1, 99],
        [99, 1, 99, 1, 99, 99, 99, 1, 99],
        [1, 1, 99, -1, 1, 1, 1, 3, 99],
        [-2, 99, 99, 1, 99, 99, 99, 1, 1],
        [1, 99, 1, -1, 1, 1, 1, 1, 99],
        [1, 99, 99, 99, 99, 2, 99, 1, 99],
        [0, 1, 3, 1, 1, 1, 99, 1, 1]
    ]
    return laberinto

def mostrar_laberinto(laberinto):
    for i in range(len(laberinto)):
        linea = ""
        for j in range(len(laberinto[i])):
            celda = laberinto[i][j]
            if i == 8 and j == 0:
                linea += "  F "
            elif i == 0 and j == 8:
                linea += "  L "
            elif celda == -999:
                linea += "  * "
            else:
                linea += f"{celda:3} "
        print(linea)

def es_movimiento_valido(laberinto, fila, columna, visitado, energia):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
        return False
    
    if laberinto[fila][columna] == 99:
        return False
    
    if visitado[fila][columna]:
        return False
    
    costo = laberinto[fila][columna]
    if costo > 0 and energia - costo < 0:
        return False
    
    return True

def buscar_camino(laberinto, fila, columna, fila_final, columna_final, energia, visitado, camino):
    if fila == fila_final and columna == columna_final:
        return True
    
    visitado[fila][columna] = True
    camino[fila][columna] = -999
    
    costo = laberinto[fila][columna]
    if costo != 0:
        energia = energia - costo
    
    movimientos = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    
    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]
        
        if es_movimiento_valido(laberinto, nueva_fila, nueva_columna, visitado, energia):
            if buscar_camino(laberinto, nueva_fila, nueva_columna, fila_final, columna_final, energia, visitado, camino):
                return True
    
    visitado[fila][columna] = False
    camino[fila][columna] = laberinto[fila][columna]
    
    return False

def resolver_laberinto():
    laberinto = crear_laberinto()
    
    fila_inicio = 8
    columna_inicio = 0
    fila_final = 0
    columna_final = 8
    energia_inicial = 50
    
    print("LABERINTO ORIGINAL:")
    mostrar_laberinto(laberinto)
    print()
    
    filas = len(laberinto)
    columnas = len(laberinto[0])
    visitado = [[False for j in range(columnas)] for i in range(filas)]
    camino = copy.deepcopy(laberinto)
    
    resultado = buscar_camino(laberinto, fila_inicio, columna_inicio, fila_final, columna_final, energia_inicial, visitado, camino)
    
    if resultado:
        print("RESULTADO: Se logro salir del laberinto")
        print()
        print("CAMINO DE SALIDA:")
        mostrar_laberinto(camino)
    else:
        print("RESULTADO: No se logro salir del laberinto")

resolver_laberinto()