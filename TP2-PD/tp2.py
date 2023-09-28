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
        for i in range(1, len(matriz_optima[0])):
            if i == 1:
                matriz_optima[i][j] = min(energia_disponible[i - 1], energia_demandada[j]) + max(obtener_columna(matriz_optima, j - 2))
            else:
                matriz_optima[i][j] = min(energia_disponible[i - 1], energia_demandada[j]) + matriz_optima[i - 1][j - 1]

    for i in range(len(matriz_optima)):
        print(matriz_optima[i])

    return max(obtener_columna(matriz_optima, len(matriz_optima[0]) - 1))

def main():
    e = [36,2, 78,	19,	59,	76,	65,	64,	33,	41]
    s = [63, 61, 49, 41, 40,38, 23, 17, 13, 10]

    print(optimo_entrenamientos(e, s))

if __name__ == '__main__':
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('50.txt')
    print(optimo_entrenamientos(energia_demandada, energia_disponible))

