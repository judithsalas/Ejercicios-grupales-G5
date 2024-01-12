def aVeryBigSum(matriz):
    # Usa la función sum() para sumar todos los elementos de la matriz.
    suma_total = sum(sum(fila) for fila in matriz)
    return suma_total

def main():
    # Solicitar al usuario la dimensión de la matriz
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    # Inicializar la matriz con ceros
    matriz = [[0] * columnas for _ in range(filas)]

    # Solicitar al usuario ingresar los elementos de la matriz
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))

    # Calcular la suma de los elementos de la matriz utilizando la función aVeryBigSum
    suma_total = aVeryBigSum(matriz)

    # Mostrar el resultado en consola
    print(f"La suma de todos los elementos de la matriz es: {suma_total}")

if __name__ == '__main__':
    main()
