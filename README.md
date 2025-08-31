# Laboratorio_1_IA

Este repositorio contiene una colección de implementaciones que abordan problemas clásicos de búsqueda en inteligencia artificial y modelado de sistemas basados en estados. Los ejemplos ilustran diferentes enfoques para resolver problemas que involucran espacios de estados discretos, transiciones entre estados, y la búsqueda de soluciones óptimas o factibles. Estos conceptos son fundamentales en áreas como la planificación autónoma, la simulación de agentes inteligentes y la resolución de problemas de optimización.

## Descripción de los Archivos
* **8_Puzzle.py**
Implementa la resolución del clásico juego 8-puzzle utilizando el algoritmo A* con la heurística de distancia Manhattan. Incluye verificación de solucionabilidad mediante el análisis de paridad de inversiones y genera secuencias óptimas de movimientos para transformar un estado inicial en un estado meta.

* **Laberinto_3x3.py**
Modela un entorno de laberinto en una grilla 3x3 con obstáculos. Implementa búsqueda en amplitud (BFS) para encontrar caminos mínimos entre puntos, demostrando el concepto de espacios de estados, funciones de transición, y la reconstrucción de rutas óptimas.

* **Problema_Lampara.py**
Un ejemplo minimalista de sistema basado en estados finitos, donde una lámpara puede estar encendida o apagada. Ilustra conceptos básicos de estados, acciones disponibles, y transiciones entre estados.

* **Buscando_Tesoro.py**
Simula un pirata buscando tesoros en un grid 3x3. Implementa movimientos restringidos por los límites del grid y demuestra la ejecución de secuencias de acciones predefinidas, mostrando cómo las acciones afectan el estado del sistema.

* **Mascota_Virtual.py**
Modela una mascota virtual con estados emocionales (contenta/triste) y acciones disponibles dependiendo del estado actual. Ejemplifica cómo las acciones pueden tener diferentes efectos según el contexto y cómo diseñar sistemas reactivos simples.

* **Laberinto_2x2.py**
Una versión simplificada de laberinto en grid 2x2, enfocada en demostrar los conceptos de tabla de transiciones, movimientos válidos, y búsqueda de caminos con restricciones de movimiento (solo derecha y abajo).

## Consideraciones Generales
Estas implementaciones destacan varios principios importantes en inteligencia artificial y modelado de sistemas:

### **1-Representación del conocimiento:** La importancia de elegir una representación adecuada de estados y acciones

### **2-Algoritmos de búsqueda:** Diferentes estrategias (A*, BFS) para explorar espacios de estados

### **3-Heurísticas:** El diseño de funciones heurísticas admisibles para guiar búsquedas informadas

### **4-Validación:** Verificación de precondiciones como la solucionabilidad de problemas

### **5-Optimalidad:** Garantía de encontrar soluciones óptimas cuando existen

Estos ejemplos sirven como base para entender problemas más complejos en planificación autónoma, simulación de agentes, y sistemas de decisión.
