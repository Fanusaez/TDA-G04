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