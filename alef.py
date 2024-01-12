import sys

def calculate_probabilities(n, m, labyrinth, tunnels):
    dp = [[0.0 for _ in range(m)] for _ in range(n)]#usamos dp para calcular los distintos caminos y luego sumar las probabilidades
    
    start_i, start_j = None, None #busca la posicion de la rana (A)
    for i in range(n):
        for j in range(m):
            if labyrinth[i][j] == 'A':
                start_i, start_j = i, j
                break
        if start_i is not None:
            break
    
    dp[start_i][start_j] = 1.0  # La rana comienza con probabilidad 1.0 en la casilla inicial
    tunnel_entries = set()  #restricion para que cada celda libre solo pueda tener una entrada a un tunel
    for tunnel in tunnels:
        (i1, j1), (i2, j2) = tunnel

        #restricciones 
        if (i1, j1) in tunnel_entries or (i2, j2) in tunnel_entries:
            print("Error: Cada celda libre puede contener como máximo una entrada a un túnel.")
            sys.exit()
        if abs(i1 - i2) <= 1 and abs(j1 - j2) <= 1:
            print("Error: Los túneles no pueden conectar celdas adyacentes.")
            sys.exit()
        tunnel_entries.add((i1, j1))
        tunnel_entries.add((i2, j2))

    for i in range(n):
        for j in range(m):
            if labyrinth[i][j] == '#': #si hay un obstaculo, se sigue buscando
                continue
            if labyrinth[i][j] == '%':
                return dp[i][j] #devuelve la probabilidad al llegar a la salida
            
            free_neighbors = sum(1 for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] #las cuatro opciones para que se mueva la rana
                    if 0 <= i + dx < n and 0 <= j + dy < m and labyrinth[i + dx][j + dy] != '#') #condiciones para no salir del laberinto
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_i, new_j = i + dx, j + dy #nuevas coordenadas
                if 0 <= new_i < n and 0 <= new_j < m and labyrinth[new_i][new_j] != '#': #mira si hay obstaculo + restriciones 
                    if (new_i, new_j) in [(i, j) for tunnel in tunnels for i, j in tunnel]:
                        for tunnel in tunnels: #bucle para calcular las probabilidades a la salida del tunel
                            (i1, j1), (i2, j2) = tunnel
                            if (0 <= i1 <= n and 0 <= j1 <= m and 0 <= i2 <= n and 0 <= j2 <= m): #restriciones para que el tunel este en el laberinto
                                if (i1, j1) == (new_i, new_j):
                                    dp[i1][j1] += dp[i][j] / free_neighbors
                                elif (i2, j2) == (new_i, new_j):
                                    dp[i2][j2] += dp[i][j] / free_neighbors
                    else:
                        dp[new_i][new_j] += dp[i][j] / free_neighbors

    return 0.0 #si en todas las posibilidades no se puede salir del laberinto

if __name__ == '__main__':
    print("\nIngrese las dimensiones del laberinto (nxm) y el numero de tuneles : ")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0]) #definimos las variables 
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    if not (1 <= n <= 19 and 1 <= m <= 19 and n * m > 2 * k): #restriciones para no tener un laberinto demasiado grande y espacio suficiente para tuneles
        print("Las dimensiones del laberinto no cumplen con las restricciones.")
        sys.exit()

    labyrinth = [] #para hacer el laberinto con inputs
    print(f"Ingrese los {m} elementos en las {n} filas")
    for _ in range(n):
        row_input = input().rstrip()
        labyrinth.append(row_input)
    if sum(row.count('A') for row in labyrinth) != 1:#restriciones para que solo haya un A
        print("Error: La celda 'A' debe aparecer exactamente una vez en el laberinto.")
        sys.exit()
    
    tunnels = []
    if k > 0:# si hay tunnel 
        print("\nIngrese las coordenadas de los tunneles (i1 j1 i2 j2): ")
        for _ in range(k):
            second_multiple_input = input().rstrip().split()
            i1 = int(second_multiple_input[0])
            j1 = int(second_multiple_input[1])
            i2 = int(second_multiple_input[2])
            j2 = int(second_multiple_input[3])
            tunnels.append(((i1, j1), (i2, j2)))

    probability_escape = calculate_probabilities(n, m, labyrinth, tunnels)
    print(f"\nLa probabilidad de escape de la rana Alef es: {probability_escape}")
