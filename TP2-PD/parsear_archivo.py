def obtener_energia_demandada_y_disponible(path_archivo):
    # El formato de los sets de datos es:
    # En la primera línea el valor de la cantidad de días a considerar (n)
    # En las siguientes n líneas, las ganancias de dichos días (nuestros e_i).
    # En las siguientes n líneas, la energía con la que se cuenta al día 1, 2, 3, ..., n de estar entrenando sin haber descansando previamente (nuestros s_i).

    with open(path_archivo) as archivo:
        lineas = archivo.readlines()
        n = int(lineas[0])
        e = [int(lineas[i]) for i in range(1, n + 1)]
        s = [int(lineas[i]) for i in range(n + 1, 2 * n + 1)]

    return e, s

def obtener_resultado(path_archivo):
    """Dado un archivo con el siguiente formato:
    En la primera línea el nombre del set de datos
    En la segunda linea la ganancia máxima obtenible con el formato: "Ganancia maxima: <ganancia>"
    En la tercera línea la lista de entrenamientos con el formato: "Plan de entrenamiento: Descanso, Entreno, Entreno, ..."
    Devuelve un diccionario que tiene como clave el nombre del set de datos y como valor una tupla con la ganancia máxima
    y el plan de entrenamiento en una lista de strings.
    Luego de esas tres lineas hay una linea en blanco y luego comienza el siguiente set de datos.
    """
    with open(path_archivo) as archivo:
        lineas = archivo.readlines()
        resultado = {}
        i = 0
        while i < len(lineas):
            nombre_set = lineas[i].strip()
            ganancia_maxima = int(lineas[i + 1].split(": ")[1])
            plan_entrenamiento = lineas[i + 2].split(": ")[1].strip().split(", ")
            resultado[nombre_set] = (ganancia_maxima, plan_entrenamiento)
            i += 4
    return resultado
