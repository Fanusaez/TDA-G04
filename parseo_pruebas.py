def obtener_tiempos_de_archivo(path: str) -> (list[int | float], list[int | float]):
    """Dado un path con un archivo con el formato: S_i, A_i
    donde i es el numero de partido, devuelve dos listas:
    s: lista de lo que tarda scaloni en revisar cada rival
    a: lista de lo que tarda los ayudantes en revisar cada rival
    """
    s = []
    a = []
    # Ignoro la primera linea que tiene los nombres de las columnas
    with open(path) as f:
        next(f)
        for line in f:
            s_i, a_i = line.split(',')
            s.append(int(s_i))
            a.append(int(a_i))
    return s, a
