def obtener_orden_minimo(s: list[int | float], a: list[int | float]) -> list[int]:
    """
    :param s: lista de lo que tarda scaloni en revisar cada rival
    :param a: lista de lo que tarda los ayudantes en revisar cada rival
    :return: lista con el orden tal que el tiempo total sea el minimo
    """
    return sorted(range(len(a)), key=lambda k: a[k], reverse=True) # O(n log n)

def obtener_tiempo_minimo(s: list[int | float], a: list[int | float]) -> list[int]:
    """
    :param s: lista de lo que tarda scaloni en revisar cada rival
    :param a: lista de lo que tarda los ayudantes en revisar cada rival
    :return: lista con el orden tal que el tiempo total sea el minimo
    """
    orden_minimo = obtener_orden_minimo(s, a)
    tiempo_total = 0
    tiempo_total_scaloni = 0
    for i in orden_minimo: # O(n)
        tiempo_total_scaloni += s[i]
        tiempo_total = max(tiempo_total, tiempo_total_scaloni + a[i])
    return tiempo_total
