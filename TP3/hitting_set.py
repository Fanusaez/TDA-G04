from parser_casos import parsear_archivo


def es_solucion(subconjuntos, asignacion_actual):
    for subconjunto in subconjuntos:
        contiene_elemento = False
        for elemento in subconjunto:
            if elemento in asignacion_actual:
                contiene_elemento = True
                break
        if not contiene_elemento:
            return False
    return True


def _hitting_set(universo, subconjuntos, indice_elemento, asignacion_actual, mejor_asignacion):
    # Poda, si la asignacion actual es peor que la mejor asignacion, no sigo
    if mejor_asignacion and len(asignacion_actual) > len(mejor_asignacion):
        return mejor_asignacion

    # Devuelvo mejor solcion hasta el momento si es que la asignacion actual es solucion
    if es_solucion(subconjuntos, asignacion_actual):
        if not mejor_asignacion or len(asignacion_actual) < len(mejor_asignacion):
            return asignacion_actual
        else:
            return mejor_asignacion

    if indice_elemento >= len(universo):
        return mejor_asignacion

    # Llamada recursiva con asignacion_actual actualizada
    resultado = _hitting_set(universo, subconjuntos, indice_elemento + 1, asignacion_actual + [universo[indice_elemento]], mejor_asignacion)

    # Actualización de mejor_asignacion
    if not mejor_asignacion or len(resultado) < len(mejor_asignacion):
        mejor_asignacion = resultado

    # Llamada recursiva sin modificar asignacion_actual
    resultado = _hitting_set(universo, subconjuntos, indice_elemento + 1, asignacion_actual, mejor_asignacion)

    # Actualización de mejor_asignacion
    if resultado and (not mejor_asignacion or len(resultado) < len(mejor_asignacion)):
        mejor_asignacion = resultado

    return mejor_asignacion


def hitting_set(universo, subconjuntos):
    return _hitting_set(universo, subconjuntos, 0, [], [])

