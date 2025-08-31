# Parámetros del mundo
GRID_MIN = 0
GRID_MAX = 2   # coordenadas van de 0 a 2 inclusive (3x3)

# Estado inicial y meta
estado_inicial = (0, 0)
estado_meta    = (2, 2)

# Acciones posibles y sus efectos sobre (x,y)
ACCIONES = {
    "ARRIBA":    (0,  1),
    "ABAJO":     (0, -1),
    "DERECHA":   (1,  0),
    "IZQUIERDA": (-1, 0),
}

def dentro_grid(pos):
    x, y = pos
    return GRID_MIN <= x <= GRID_MAX and GRID_MIN <= y <= GRID_MAX

def acciones_disponibles(estado):
    """Devuelve la lista de acciones válidas desde el estado (x,y) según los límites del grid."""
    disponibles = []
    x, y = estado
    for nombre, (dx, dy) in ACCIONES.items():
        nuevo = (x + dx, y + dy)
        if dentro_grid(nuevo):
            disponibles.append(nombre)
    return disponibles

def cambiar_estado(estado, accion):
    """Aplica la acción y devuelve el nuevo estado (si la acción no es válida, devuelve el mismo estado)."""
    if accion not in ACCIONES:
        return estado
    x, y = estado
    dx, dy = ACCIONES[accion]
    nuevo = (x + dx, y + dy)
    if dentro_grid(nuevo):
        return nuevo
    else:
        return estado

def imprimir_estado(estado):
    print(f"Pirata en: {estado}")

estado = estado_inicial
imprimir_estado(estado)
print("Acciones disponibles:", acciones_disponibles(estado))

secuencia = ["ARRIBA", "ARRIBA", "DERECHA", "DERECHA"]
#Se puede modificar la secuencia de tal manera que no se llegue al objetivo, o se llegue con más pasos

for a in secuencia:
    print("Ejecutando:", a)
    estado = cambiar_estado(estado, a)
    imprimir_estado(estado)
    if estado == estado_meta:
        print("¡Tesoro encontrado!")
        break
else:
    print("Secuencia terminada. Tesoro no alcanzado.")
