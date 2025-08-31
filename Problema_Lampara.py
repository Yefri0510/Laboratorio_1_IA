#Problema de la lámpara (estados y acciones)

#Tenemos una que puede estar ENCENDIDA o APAGADA y queremos cambiarla de estado

#Defini los estados posibles
estados = ["ENCENDIDA", "APAGADA"]

#Definir el estado inicial y el estado meta
estado_actual = "APAGADA"
estado_meta = "ENCENDIDA"

#Definir las acciones posibles
def acciones_disponibles(estado):
    return ["PRENDER", "APAGAR"] #Siempre disponibles

#Crear una función para cambair de estado
def cambiar_estado(estado, accion):
    if accion == "PRENDER":
        return "ENCENDIDA"
    elif accion == "APAGAR":
        return "APAGADA"

#Simular
print(f"Estado inicial: {estado_actual}")
accion = "PRENDER"
estado_actual = cambiar_estado(estado_actual, accion)
print(f"Después de: {accion}: {estado_actual}")

#Verificar si llegamos al estado meta
if estado_actual == estado_meta:
    print("¡Meta alcanzada!")

        
    

