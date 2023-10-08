from parsear_archivo import obtener_energia_demandada_y_disponible


def obtener_columna(matriz, columna):
    return [fila[columna] for fila in matriz]


def optimo_entrenamientos(energia_demandada, energia_disponible):
    """Dadas las listas de energía demandada y disponible, devuelve la máxima energía que se puede obtener entrenando"""
    matriz_optima = obtener_matriz_optima(energia_demandada, energia_disponible)
    return max(obtener_columna(matriz_optima, len(matriz_optima[0]) - 1))


def obtener_matriz_optima(energia_demandada, energia_disponible):
    matriz_optima = [[0 for _ in range(len(energia_demandada))] for _ in range(len(energia_disponible))]
    matriz_optima[0][0] = min(energia_demandada[0], energia_disponible[0])
    matriz_optima[1][1] = min(energia_demandada[1], energia_disponible[0])
    for i in range(1, len(matriz_optima[0])):
        matriz_optima[0][i] = matriz_optima[0][i - 1] + min(energia_demandada[i], energia_disponible[i])
    for j in range(2, len(matriz_optima)):
        for i in range(1, j + 1):
            if i == 1:
                matriz_optima[i][j] = min(energia_disponible[i - 1], energia_demandada[j]) + max(
                    obtener_columna(matriz_optima, j - 2))
            else:
                matriz_optima[i][j] = min(energia_disponible[i - 1], energia_demandada[j]) + matriz_optima[i - 1][j - 1]
    return matriz_optima

def obtener_lista_entrenamientos(energia_demandada, energia_disponible):
    """Dadas las listas de energía demandada y disponible, devuelve una lista que en el i-ésimo elemento dice "Entreno"
    o "Descanso" según corresponda para optimizar la energía obtenida en el n-ésimo día"""
    matriz_optima = obtener_matriz_optima(energia_demandada, energia_disponible)
    lista_entrenamientos = ["Entreno"] * len(matriz_optima)
    j = len(matriz_optima) - 1
    while j > 0:
        indice_maximo = obtener_columna(matriz_optima, j).index(max(obtener_columna(matriz_optima, j)))
        j -= indice_maximo
        if indice_maximo != 0:
            lista_entrenamientos[j] = "Descanso"
        j -= 1
    return lista_entrenamientos
