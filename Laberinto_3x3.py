from collections import deque

# -------------------------
# 1) Definición del espacio
# -------------------------
GRID_MIN = 0
GRID_MAX = 2   # 3x3: coordenadas 0..2

STATES = [(x,y) for y in range(GRID_MIN, GRID_MAX+1) for x in range(GRID_MIN, GRID_MAX+1)]
START = (0,0)
GOAL  = (2,2)

# Acciones: ARRIBA, ABAJO, IZQUIERDA, DERECHA
ACTIONS = {
    "UP":    (0, -1),
    "DOWN":  (0,  1),
    "LEFT":  (-1, 0),
    "RIGHT": (1,  0),
}

# -------------------------
# 2) Funciones auxiliares
# -------------------------
def dentro_grid(pos):
    x, y = pos
    return GRID_MIN <= x <= GRID_MAX and GRID_MIN <= y <= GRID_MAX

def aplicar_accion(pos, accion):
    """Devuelve la nueva posición (sin comprobar límites ni obstáculos)."""
    dx, dy = ACTIONS[accion]
    return (pos[0] + dx, pos[1] + dy)

# -------------------------
# 3) Tabla de transiciones
# -------------------------
def construir_tabla_transiciones(obstaculos=set()):
    """
    Devuelve dict: (estado, accion) -> (resultado, nuevo_estado)
    resultado: 'OK', 'BLOQUEADO', 'FUERA_LIMITE'
    """
    tabla = {}
    for s in STATES:
        for a in ACTIONS:
            nuevo = aplicar_accion(s, a)
            if not dentro_grid(nuevo):
                tabla[(s,a)] = ('FUERA_LIMITE', s)
            elif nuevo in obstaculos:
                tabla[(s,a)] = ('BLOQUEADO', s)
            else:
                tabla[(s,a)] = ('OK', nuevo)
    return tabla

# -------------------------
# 4) Función mover()
# -------------------------
def mover(estado, accion, obstaculos=set()):
    """
    Intenta mover desde 'estado' con 'accion' considerando 'obstaculos'.
    Retorna: (flag_moved, nuevo_estado, mensaje)
    """
    if accion not in ACTIONS:
        return False, estado, "ACCION_INVALIDA"
    tabla = construir_tabla_transiciones(obstaculos)
    resultado, nuevo = tabla[(estado, accion)]
    if resultado == 'OK':
        return True, nuevo, 'OK'
    else:
        return False, estado, resultado

# -------------------------
# 5) BFS: búsqueda de ruta mínima
# -------------------------
def bfs_ruta(inicio, objetivo, obstaculos=set()):
    """
    BFS que devuelve lista de (estado, accion_que_llego_a_este) desde inicio (accion None)
    a objetivo. Retorna None si no existe ruta.
    """
    if inicio == objetivo:
        return [(inicio, None)]

    tabla = construir_tabla_transiciones(obstaculos)
    cola = deque([inicio])
    padre = {inicio: (None, None)}  # estado -> (padre, accion)
    while cola:
        actual = cola.popleft()
        for accion in ACTIONS:
            res, vecino = tabla[(actual, accion)]
            if res != 'OK':
                continue
            if vecino not in padre:
                padre[vecino] = (actual, accion)
                cola.append(vecino)
                if vecino == objetivo:
                    # reconstruir camino
                    camino = []
                    nodo = objetivo
                    while nodo is not None:
                        p, act = padre[nodo]
                        camino.append((nodo, act))
                        nodo = p
                    camino.reverse()
                    return camino
    return None

# -------------------------
# 6) Visualización del mapa
# -------------------------
def imprimir_mapa(obstaculos=set(), start=START, goal=GOAL):
    print("Mapa (x izq->der, y arriba->abajo):")
    for y in range(GRID_MIN, GRID_MAX+1):
        fila = []
        for x in range(GRID_MIN, GRID_MAX+1):
            p = (x,y)
            if p == start:
                fila.append("S")
            elif p == goal:
                fila.append("G")
            elif p in obstaculos:
                fila.append("#")
            else:
                fila.append(".")
        print(" ".join(fila))
    print()

def imprimir_ruta(ruta):
    if ruta is None:
        print("  No existe ruta.")
        return
    pasos = len(ruta) - 1
    print(f"  Ruta encontrada en {pasos} movimientos:")
    for est, acc in ruta:
        if acc is None:
            print(f"    Inicio: {est}")
        else:
            print(f"    -> Acción: {acc:6}  Estado: {est}")
    print()

# -------------------------
# 7) Recompensas (ejemplo)
# -------------------------
REWARDS = {s: -1 for s in STATES}  # coste por paso
REWARDS[GOAL] = 10                 # recompensa por alcanzar meta

# -------------------------
# 8) Escenarios de prueba
# -------------------------
def prueba_escenario(obstaculos=set()):
    print("Obstáculos:", obstaculos)
    imprimir_mapa(obstaculos)
    tabla = construir_tabla_transiciones(obstaculos)

    # 1) Encontrar camino de START a (0,1) (tarea solicitada)
    objetivo_inter = (0,1)
    print(f"Buscando camino de {START} a {objetivo_inter}:")
    ruta_inter = bfs_ruta(START, objetivo_inter, obstaculos)
    imprimir_ruta(ruta_inter)

    # 2) Encontrar camino de START a GOAL
    print(f"Buscando camino de {START} a {GOAL}:")
    ruta_goal = bfs_ruta(START, GOAL, obstaculos)
    imprimir_ruta(ruta_goal)
    print("-"*50 + "\n")

if __name__ == "__main__":
    print("=== Laberinto 3x3 - Pruebas ===\n")

    # ESCENARIO A: Sin obstáculos
    prueba_escenario(obstaculos=set())

    # ESCENARIO B: Obstáculo en (0,1) (tarea te pide probar esto)
    prueba_escenario(obstaculos={(0,1)})

    # ESCENARIO C: Obstáculo en (0,1) y en (1,0) (bloquea vías cortas)
    prueba_escenario(obstaculos={(0,1), (1,0)})
