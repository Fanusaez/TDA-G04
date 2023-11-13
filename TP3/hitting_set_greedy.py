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

def contar_apariciones(subconjuntos, apariciones):
    for subconjunto in subconjuntos:
        for jugador in subconjunto:
            if jugador not in apariciones:
                apariciones[jugador] = 1
            else:
                apariciones[jugador] += 1
    return apariciones


def eliminar_subconjuntos_con_jugador(subconjuntos, jugador):
    nuevo_subconjunto = []

    for subconjunto in subconjuntos:
        if jugador not in subconjunto:
            nuevo_subconjunto.append(subconjunto)

    return nuevo_subconjunto


def hitting_set_greedy(universo, subconjuntos, k):
    asignacion = []
    apariciones = {}
    while not es_solucion(subconjuntos, asignacion) and k > len(asignacion):
        apariciones = contar_apariciones(subconjuntos, apariciones)
        apariciones_ordenado = dict(sorted(apariciones.items(), key=lambda item: item[1], reverse=True))
        asignacion.append(next(iter(apariciones_ordenado)))
        if es_solucion(subconjuntos, asignacion) and len(asignacion) <= k:
            return asignacion
        subconjuntos = eliminar_subconjuntos_con_jugador(subconjuntos, asignacion[-1])

    return asignacion

