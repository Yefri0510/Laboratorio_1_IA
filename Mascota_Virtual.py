# Problema de la mascota virtual (estados y acciones)

# La mascota puede estar CONTENTA o TRISTE

# Definir los estados posibles
estados = ["CONTENTO", "TRISTE"]

# Definir el estado inicial y el estado meta
estado_actual = "TRISTE"
estado_meta = "CONTENTO"

# Definir las acciones posibles según el estado
def acciones_disponibles(estado):
    if estado == "TRISTE":
        return ["DAR_COMIDA"]   # cuando está triste se le puede dar comida
    elif estado == "CONTENTO":
        return ["NO_HACER_NADA"]  # cuando está feliz no necesita nada
    else:
        return []

# Función para cambiar de estado
def cambiar_estado(estado, accion):
    if accion == "DAR_COMIDA" and estado == "TRISTE":
        return "CONTENTO"
    elif accion == "NO_HACER_NADA" and estado == "CONTENTO":
        return "CONTENTO"
    else:
        return estado

# Simulación
print(f"Estado inicial: {estado_actual}")

acciones = acciones_disponibles(estado_actual)
print(f"Acciones disponibles: {acciones}")

# Ejecutamos una acción
accion = "DAR_COMIDA"
print(f"Acción seleccionada: {accion}")
estado_actual = cambiar_estado(estado_actual, accion)
print(f"Después de la acción: {estado_actual}")

# Verificar si llegamos al estado meta
if estado_actual == estado_meta:
    print("¡Meta alcanzada! La mascota está feliz")
else:
    print("La mascota sigue triste")
