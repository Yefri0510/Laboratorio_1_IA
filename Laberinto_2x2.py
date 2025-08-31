from collections import deque

# -------------------------
# 1) Definir el espacio
# -------------------------
# Grid 2x2: coordenadas x,y en {0,1}
STATES = [(0,0), (1,0), (0,1), (1,1)]
START = (0,0)
GOAL  = (1,1)

# Acciones permitidas: → (RIGHT) y ↓ (DOWN)
ACTIONS = {
    "DERECHA": (1, 0),
    "ABAJO":  (0, 1),
}

# -------------------------
# 2) Funciones auxiliares
# -------------------------
def dentro_grid(pos):
    x,y = pos
    return 0 <= x <= 1 and 0 <= y <= 1

def aplicar_accion(pos, accion):
    """Devuelve la nueva posición sin comprobar obstáculos ni límites."""
    dx, dy = ACTIONS[accion]
    return (pos[0] + dx, pos[1] + dy)

# -------------------------
# 3) Tabla de transiciones
# -------------------------
def construir_tabla_transiciones(obstaculos=set()):
    """
    Construye y devuelve un diccionario con claves (estado,accion) -> siguiente_estado o 'BLOQUEADO'
    """
    tabla = {}
    for s in STATES:
        for a in ACTIONS:
            nuevo = aplicar_accion(s, a)
            if not dentro_grid(nuevo):
                tabla[(s,a)] = ('FUERA_LIMITE', s)   # no mueve (se queda en s)
            elif nuevo in obstaculos:
                tabla[(s,a)] = ('BLOQUEADO', s)      # movimiento bloqueado por obstáculo
            else:
                tabla[(s,a)] = ('OK', nuevo)         # movimiento válido
    return tabla

# -------------------------
# 4) Función de movimiento
# -------------------------
def mover(estado, accion, obstaculos=set()):
    """
    Intenta mover desde 'estado' con 'accion'.
    Retorna (flag, nuevo_estado, mensaje)
      flag: True si movió, False si no
      nuevo_estado: estado resultante (si no se mueve devuelve estado original)
      mensaje: explicación ('OK', 'BLOQUEADO', 'FUERA_LIMITE', 'ACCION_INVALIDA')
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
# 5) Búsqueda de camino (BFS)
# -------------------------
def bfs_ruta(inicio, objetivo, obstaculos=set()):
    """
    Busca la ruta mínima (en número de acciones) de inicio a objetivo usando sólo RIGHT/DOWN
    Devuelve lista de (estado, accion_que_llego_a_este) desde inicio (accion None) a objetivo,
    o None si no hay ruta.
    """
    if inicio == objetivo:
        return [(inicio, None)]

    tabla = construir_tabla_transiciones(obstaculos)
    cola = deque([inicio])
    padre = {inicio: (None, None)}  # estado -> (padre_estado, accion)
    while cola:
        actual = cola.popleft()
        for accion in ACTIONS:
            estado_res = tabla[(actual, accion)]
            if estado_res[0] != 'OK':
                continue  # movimiento inválido (fuera/obstáculo)
            vecino = estado_res[1]
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
# 6) Recompensas (diccionario)
# -------------------------
REWARDS = {s: -1 for s in STATES}   # coste por paso
REWARDS[GOAL] = 10                  # recompensa por alcanzar meta
# Podemos añadir penalizaciones por intentar moverse a obstáculo (lo manejamos en mensajes)

# -------------------------
# 7) Pruebas y demostración
# -------------------------
def imprimir_tabla(tabla):
    print("Tabla de transiciones (estado, acción) -> (resultado, nuevo_estado):")
    for s in STATES:
        for a in ACTIONS:
            print(f"  {s}, {a} -> {tabla[(s,a)]}")
    print()

def imprimir_ruta(ruta):
    if ruta is None:
        print("  No existe ruta.")
        return
    pasos = len(ruta)-1
    print(f"  Ruta encontrada en {pasos} movimientos:")
    for est, acc in ruta:
        if acc is None:
            print(f"    Inicio: {est}")
        else:
            print(f"    -> Acción: {acc:6}  Estado: {est}")
    print()

def prueba_scenario(obstaculos):
    print("Obstáculos:", obstaculos)
    tabla = construir_tabla_transiciones(obstaculos)
    imprimir_tabla(tabla)

    # 1) Encontrar camino desde START a (0,1)
    objetivo_intermedio = (0,1)
    print(f"Buscando camino de {START} a {objetivo_intermedio}:")
    ruta1 = bfs_ruta(START, objetivo_intermedio, obstaculos)
    imprimir_ruta(ruta1)

    # 2) Encontrar camino desde START a GOAL (1,1)
    print(f"Buscando camino de {START} a {GOAL}:")
    ruta2 = bfs_ruta(START, GOAL, obstaculos)
    imprimir_ruta(ruta2)
    print("-"*40 + "\n")

if __name__ == "__main__":
    print("Mundo 2x2 - Pruebas\n")

    # ESCENARIO A: Sin obstáculos
    prueba_scenario(obstaculos=set())

    # ESCENARIO B: Agregar obstáculo en (0,1)
    prueba_scenario(obstaculos={(0,1)})
