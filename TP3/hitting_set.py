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
        return asignacion_actual

    if indice_elemento >= len(universo):
        return []

    asignacion_actual.append(universo[indice_elemento])
    resultado = _hitting_set(universo, subconjuntos, k, indice_elemento + 1, asignacion_actual)

    if len(resultado) > 0:
        return resultado

    asignacion_actual.pop()

    return _hitting_set(universo, subconjuntos, k, indice_elemento + 1, asignacion_actual)


def hitting_set(universo, subconjuntos, k):
    return _hitting_set(universo, subconjuntos, k, 0, [])


def main():
    """conjunto_universo = ["A", "B", "C", "D", "F"]
    subconjuntos = [["A","B"], ["B", "C"], ["B","D"], ["D", "F"]]
    k = 5

    print(hitting_set(conjunto_universo, subconjuntos, k))
    """
    universo = parsear_archivo("TP3/20.txt")[0]
    subconjuntos = parsear_archivo("TP3/20.txt")[1]
    print(universo)
    print(subconjuntos)
    k = 5
    print(hitting_set(universo, subconjuntos, k))


if __name__ == '__main__':
    main()

