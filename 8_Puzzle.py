from heapq import heappush, heappop

def is_solvable(state, goal):
    """Compara la paridad de inversiones entre state y goal (3x3 -> solo inversiones)."""
    def inv_count(arr):
        a = [x for x in arr if x != 0]
        inv = 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[i] > a[j]:
                    inv += 1
        return inv
    return (inv_count(state) % 2) == (inv_count(goal) % 2)

def manhattan(state, goal_pos):
    """Heurística: suma de distancias Manhattan de cada ficha respecto a su posición objetivo.
       state: tupla de 9 ints (0..8), goal_pos: dict value->index objetivo."""
    dist = 0
    for idx, val in enumerate(state):
        if val == 0: 
            continue
        goal_idx = goal_pos[val]
        r1, c1 = divmod(idx, 3)
        r2, c2 = divmod(goal_idx, 3)
        dist += abs(r1 - r2) + abs(c1 - c2)
    return dist

def neighbors(state):
    """Genera (nuevo_estado, movimiento) desde el estado actual.
       movimiento: 'arriba','abajo','izquierda','derecha' refiriéndose al movimiento del hueco."""
    moves = []
    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)
    directions = {
        'arriba':    (-1, 0),
        'abajo':  ( 1, 0),
        'izquierda':  ( 0,-1),
        'derecha': ( 0, 1),
    }
    for name, (dr, dc) in directions.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            swap_idx = nr * 3 + nc
            lst = list(state)
            lst[zero_idx], lst[swap_idx] = lst[swap_idx], lst[zero_idx]
            moves.append((tuple(lst), name))
    return moves

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        current, move = came_from[current]
        path.append((current, move))
    path.reverse()
    return path

def a_star(start, goal):
    """A* que devuelve la lista de estados desde start (excluyendo) hasta goal (incluyendo).
       Retorna None si no hay solución dentro de la búsqueda."""
    if start == goal:
        return []

    # Precomputar posiciones objetivo para la heurística
    goal_pos = { val: idx for idx, val in enumerate(goal) }

    open_heap = []
    g_score = {start: 0}
    f_score = {start: manhattan(start, goal_pos)}
    heappush(open_heap, (f_score[start], 0, start))  # (f, tie, state)
    came_from = {}   # map state -> (parent_state, move_that_led_here)
    closed = set()
    tie = 0

    while open_heap:
        _, _, current = heappop(open_heap)
        if current == goal:
            # reconstruir ruta: queremos la secuencia de (estado, movimiento) desde start hacia goal
            path = reconstruct_path(came_from, current)
            # agregar estado final con movimiento 'goal' para claridad
            path.append((current, 'goal'))
            return path

        closed.add(current)
        for neigh, move in neighbors(current):
            if neigh in closed:
                continue
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neigh, float('inf')):
                came_from[neigh] = (current, move)
                g_score[neigh] = tentative_g
                f = tentative_g + manhattan(neigh, goal_pos)
                if neigh not in (s for _, _, s in open_heap):
                    tie += 1
                    heappush(open_heap, (f, tie, neigh))

    return None  # sin solución encontrada

def print_state(state):
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(' '.join(str(x) if x != 0 else '_' for x in row))
    print()

# Ejemplo de uso
if __name__ == "__main__":
    # EJEMPLO (tomado de la imagen):
    # Estado inicial: 2 8 3 / 1 6 4 / 7 0 5  (0 = hueco)
    initial = (2,8,3, 1,6,4, 7,0,5)
    # Estado final (meta de la imagen): 1 2 3 / 8 0 4 / 7 6 5
    goal    = (1,2,3, 8,0,4, 7,6,5)

    print("Estado inicial:")
    print_state(initial)
    print("Estado objetivo:")
    print_state(goal)

    if not is_solvable(initial, goal):
        print("Este 8-puzzle NO es resolvible (paridad diferente).")
    else:
        print("Buscando solución (A* con Manhattan)...")
        path = a_star(initial, goal)
        if path is None:
            print("No se encontró solución (o se agotó la búsqueda).")
        else:
            steps = len(path) - 1  # la última entrada es 'goal'
            print(f"Solución encontrada en {steps} movimientos:\n")
            # imprimir secuencia: start -> ... -> goal
            current = initial
            print_state(current)
            for (st, mv) in path:
                # st es el estado al que se llegó con el movimiento mv
                print(f"Movimiento: {mv}")
                print_state(st)
