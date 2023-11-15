from parser_casos import parsear_archivo
from hitting_set import es_solucion


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


def hitting_set_greedy(subconjuntos):
    # Lista para la asignacion final
    asignacion = []

    # Diccionario para contar las apariciones de cada jugador
    apariciones = {}

    while not es_solucion(subconjuntos, asignacion):
        apariciones = contar_apariciones(subconjuntos, apariciones)

        # Ordena el diccionario de apariciones de forma descendente
        apariciones_ordenado = dict(sorted(apariciones.items(), key=lambda item: item[1], reverse=True))

        # Agrega el jugador más frecuente a la asignación
        asignacion.append(next(iter(apariciones_ordenado)))

        if es_solucion(subconjuntos, asignacion):
            return asignacion

        # Elimina los subconjuntos que contienen al último jugador agregado
        subconjuntos = eliminar_subconjuntos_con_jugador(subconjuntos, asignacion[-1])

    return asignacion

