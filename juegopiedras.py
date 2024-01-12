def jugar_piedras():
    # Solicitar al usuario ingresar el número total de piedras
    piedras_totales = int(input("Ingresa el número total de piedras: "))
    jugador_actual = 1  # Jugador 1 comienza

    print("¡Bienvenido al juego de las piedras!")
    print(f"Hay {piedras_totales} piedras en total. Cada jugador puede tomar 2, 3 o 5 piedras por turno.")

    while piedras_totales > 0:
        print(f"\nTurno del Jugador {jugador_actual}")
        piedras_a_tomar = int(input("¿Cuántas piedras quieres tomar (2, 3 o 5)? "))

        # Verificar validez del movimiento
        if piedras_a_tomar in [2, 3, 5] and piedras_a_tomar <= piedras_totales:
            piedras_totales -= piedras_a_tomar
            print(f"Jugador {jugador_actual} toma {piedras_a_tomar} piedras. Quedan {piedras_totales} piedras.")

            # Verificar si el jugador llega a 0 o 1 piedra
            if piedras_totales <= 1:
                print(f"\n¡Felicidades! Jugador {jugador_actual} gana.")
                break
        else:
            print("¡Movimiento inválido! Debes tomar 2, 3 o 5 piedras y no más de las disponibles. Inténtalo de nuevo.")
            continue

        # Cambiar al otro jugador
        jugador_actual = 3 - jugador_actual  # Alternar entre 1 y 2

if __name__ == "__main__":
    jugar_piedras()
