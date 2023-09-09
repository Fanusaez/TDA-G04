def obtener_orden_minimo(s, a):
    """
    :param s: Lista de tiempos de lo que tarda Scaloni en revisar cada rival
    :param a: Lista de tiempos de lo que tarda cada ayudante en revisar cada rival
    :return: lista con el orden tal que el tiempo total sea el minimo
    """
    return sorted(range(len(a)), key=lambda k: a[k], reverse=True) # O(n log n)

def obtener_tiempo_minimo(s, a):
    """
    :param s: lista de lo que tarda Scaloni en revisar cada rival
    :param a: lista de lo que tarda cada ayudante en revisar cada rival
    :return: El tiempo minimo que se tarda en revisar a todos los rivales
    """
    orden_minimo = obtener_orden_minimo(s, a)
    tiempo_total = 0
    tiempo_total_scaloni = 0
    for i in orden_minimo: # O(n)
        tiempo_total_scaloni += s[i]
        tiempo_total = max(tiempo_total, tiempo_total_scaloni + a[i])
    return tiempo_total
