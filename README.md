# Ejercicios grupales G5
## Grupo formado por María Muñoz, Fabiola de Arizón y Judith M.ª Salas.

### Ejecicio una suma muy grande.
El código propuesto pide al usuario los elementos de una matriz y suma todos los elementos de esta.

### Ejercicio juego de piedras

El código implementa un juego de piedras para dos jugadores, donde cada jugador puede tomar 2, 3 o 5 piedras por turno. El número total de piedras es definido por el usuario al inicio. El juego continúa alternando turnos entre los jugadores hasta que un jugador toma la última piedra, llega a 0 o 1 piedras y es declarado como el ganador.


### Ejercicio el juego de la rana Alef

Para hacer el juego de la rana en el laberinto, primero hemos importado el módulo "sys" para poder salir del programa (sys.exit) cada vez que hay un problema, por ejemplo, una restricción.

Hemos empezado creando la función calculate_probabilities fuera del bloque main porque es una función independiente que luego llamamos en el bloque principal. La función tiene 4 variables:

n, el número de filas en el laberinto
m, el número de columnas
labyrinth, una lista para almacenar los datos del laberinto dados por el usuario
tunnels, una lista que almacena las coordenadas de las entradas y salidas del/los túnel(es) dados por el usuario
Hemos utilizado dp, que representa una matriz bidimensional que se utiliza para calcular todos los posibles caminos por donde Alef puede pasar. Hemos definido entonces la posición inicial de Alef que es "A". Le hemos fijado a esa posición una probabilidad inicial de 1. Luego le hemos fijado algunas de las restricciones pedidas por el enunciado.

Cada celda libre (X) puede contener como máximo una entrada a un túnel.
Los túneles no pueden conectar celdas adyacentes.
Después hemos empezado con bucles "for in range" para definir que cuando Alef avanza:

Si encuentra un obstáculo (denotado como "#"), sigue buscando.
Si encuentra la salida (denotada como "%"), se acaba el bucle.
Luego hemos definido una variable "free_neighbors" que representa el número de vecinos accesibles (que no sea obstáculo). Hemos indicado más restricciones pedidas en el enunciado como:

i1 e i2 deben ser menores o iguales que n.
i1 e i2 deben ser menores o iguales que m.
Hemos hecho otro bucle para definir que cuando se pasa por un túnel, hay que calcular otra vez las probabilidades desde la salida. Se calcula dividiendo dp por la cantidad de free_neighbors. Si no se puede llegar a la salida, entonces la probabilidad es 0.

Entonces empieza el bloque main. Primero hemos hecho un input para preguntar al usuario las dimensiones y el número de túneles (k). Hemos definido las variables como "first_multiple_input" como pedido en el enunciado. Hemos puesto otra restricción: n y m deben ser > 20.

Luego hemos definido la lista labyrinth, hemos hecho otro input para que el usuario disponga símbolos de los elementos por fila (con for in range n(fila)). Hemos añadido otra restricción que solo puede haber un A porque solo hay una rana. Y entonces hemos definido la lista tunnel (cuando hay uno (k>0)) y definimos las otras variables "second_multiple_input" como pedido en el enunciado.

Hemos acabado llamando la función calculate_probabilities y hemos hecho un print para que del resultado de la probabilidad de que Alef se escape del laberinto.

Se va a proporcionar un ejemplo:

Ingrese las dimensiones del laberinto (nxm) y el numero de tuneles : 
3 6 1

Ingrese los 6 elementos en las 3 filas
###*##
X#XA%#
###*##

Ingrese las coordenadas de los tunneles (i1 j1 i2 j2): 
2 3 2 1

La probabilidad de escape de la rana Alef es: 0.25
