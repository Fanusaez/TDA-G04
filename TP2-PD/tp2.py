from parsear_archivo import obtener_energia_demandada_y_disponible


def obtener_columna(matriz, columna):
    return [fila[columna] for fila in matriz]


def optimo_entrenamientos(energia_demandada, energia_disponible):
    matriz_optima = [[0 for _ in range(len(energia_demandada))] for _ in range(len(energia_disponible))]
    matriz_optima[0][0] = min(energia_demandada[0], energia_disponible[0])
    matriz_optima[1][1] = min(energia_demandada[1], energia_disponible[0])

    for i in range(1, len(matriz_optima[0])):
        matriz_optima[0][i] = matriz_optima[0][i-1] + min(energia_demandada[i], energia_disponible[i])

    for j in range(2, len(matriz_optima)):
        for i in range(1, j + 1):
            if i == 1:
                matriz_optima[i][j] = min(energia_disponible[i - 1], energia_demandada[j]) + max(obtener_columna(matriz_optima, j - 2))
            else:
                matriz_optima[i][j] = min(energia_disponible[i - 1], energia_demandada[j]) + matriz_optima[i - 1][j - 1]

    return max(obtener_columna(matriz_optima, len(matriz_optima[0]) - 1))

