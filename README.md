# TDA - Teoría de Algoritmos
### Cátedra Buchwald — 2024 (2° Cuatrimestre)

Repositorio académico con implementaciones y ejercicios resueltos de la materia **Teoría y Diseño de Algoritmos** de la carrera de Ingeniería en Informática (FIUBA). Cubre las principales técnicas de diseño de algoritmos con implementaciones en **Python**.

---

## 📁 Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| [`Backtracking/`](#backtracking) | Búsqueda exhaustiva con poda |
| [`DyC/`](#divide--conquer-dyc) | Dividir y conquistar |
| [`Flujo/`](#flujo-de-redes-flujo) | Flujo en redes |
| [`PD/`](#programación-dinámica-pd) | Programación dinámica |
| [`PL/`](#programación-lineal-pl) | Programación lineal |
| [`Reduccion/`](#reducciones-reduccion) | Reducciones y problemas NP-completos |
| [`Parciales/`](#parciales) | Resolución de parciales 2024 |

---

## Backtracking

Implementaciones de algoritmos de búsqueda exhaustiva con técnicas de poda:

- **N-Reinas**: colocación de N reinas en un tablero sin conflictos.
- **Coloreo de grafos**: asignación de colores a vértices con restricciones de adyacencia.
- **Ciclo hamiltoniano**: búsqueda de ciclos que recorren todos los vértices.
- **Conjunto dominante / Cobertura de vértices / Conjunto independiente**: problemas clásicos de grafos.
- **Isomorfismo de grafos**: verificación de equivalencia estructural entre grafos.

## Divide & Conquer (`DyC/`)

Resolución de problemas mediante subdivisión recursiva:

- **Conteo de inversiones**: variante de Merge Sort para contar pares invertidos.
- **Par de puntos más cercano**: algoritmo geométrico O(n log n).
- **Búsqueda de raíces**: localización de raíces de funciones.
- **Alternancia de enteros**: otros ejercicios de práctica.

## Flujo de redes (`Flujo/`)

Algoritmos sobre redes de flujo:

- **Ford-Fulkerson / Flujo máximo**: cálculo de flujo máximo en una red.
- **Caminos aumentantes**: búsqueda de caminos en grafos residuales.
- **Emparejamiento bipartito perfecto**: matching en grafos bipartitos.
- **Caminos disjuntos**: máximo número de caminos sin aristas en común.
- **Reconstrucción de grafos**: reconstrucción a partir de grados.

## Programación Dinámica (`PD/`)

Resolución de problemas de optimización con subestructura óptima:

- **Problema de la mochila (0/1 Knapsack)**: maximización de valor con capacidad limitada.
- **Autómata celular**: simulación con estados dependientes del historial.
- **Juego de los gemelos (Twin Game)**: problema de teoría de juegos.
- **Scheduling**: planificación óptima de tareas.

## Programación Lineal (`PL/`)

Modelado y resolución de problemas como programas lineales:

- **Conjunto dominante / Cobertura de vértices**: formulación LP de problemas de grafos.
- **Mochila LP**: relajación lineal del problema de la mochila.
- **Juan el Vago**: problema clásico de la cátedra modelado como LP.
- Utilidades de grafos de soporte.

## Reducciones (`Reduccion/`)

Demostraciones de NP-completitud y cadenas de reducción:

- **Conjunto independiente ↔ Cobertura de vértices**: reducción polinomial entre problemas.
- **Ejercicios 4 al 15**: serie de reducciones entre problemas NP-completos.
- Incluye diagramas y notas explicativas (`.md`, `.png`).

## Parciales

Resolución de exámenes parciales tomados durante 2024:

- Parciales de los grupos **c0**, **c1** y **c2**.
- Incluye problemas de diversas técnicas (BT, DyC, Flujo, PD, Reducciones).

---

## 🛠️ Tecnologías

- **Lenguaje**: Python 3
- La mayoría de los ejercicios no requieren dependencias externas; los ejercicios de PL pueden requerir `scipy` o `pulp`.

---

## 📚 Sobre la materia

**TDA (Teoría y Diseño de Algoritmos)** es una materia del Departamento de Computación de la **FIUBA** (Facultad de Ingeniería, Universidad de Buenos Aires). Cubre el análisis de complejidad, paradigmas de diseño de algoritmos y teoría de NP-completitud.
