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


def _hitting_set(universo, subconjuntos, k, indice_elemento, asignacion_actual):
    if len(asignacion_actual) > k:
        return []

    if es_solucion(subconjuntos, asignacion_actual):
        return asignacion_actual[:]

    if indice_elemento >= len(universo):
        return []

    mejor_asignacion = []

    asignacion_actual.append(universo[indice_elemento])
    resultado = _hitting_set(universo, subconjuntos, k, indice_elemento + 1, asignacion_actual)
    if resultado:
        mejor_asignacion = resultado

    asignacion_actual.pop()
    resultado = _hitting_set(universo, subconjuntos, k, indice_elemento + 1, asignacion_actual)
    if resultado:
        if not mejor_asignacion or len(resultado) < len(mejor_asignacion):
            mejor_asignacion = resultado

    return mejor_asignacion

def hitting_set(universo, subconjuntos, k):
    return _hitting_set(universo, subconjuntos, k, 0, [])

