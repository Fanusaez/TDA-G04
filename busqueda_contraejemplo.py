
import random

"""Devuelve una lista de tuplas de los elementos ordenados por el tiempo que tardan los ayudantes de mayor a menor"""
def ordenar_por_mayor_tiempo_ayudantes(tuplas):
   return sorted(tuplas, key=lambda x: x[1], reverse=True)

"""Devuelve una lista de tuplas de los elementos ordenados por el tiempo que tarda Scaloni de mayor a menor"""
def ordenar_por_mayor_tiempo_scaloni(tuplas):
     return sorted(tuplas, key=lambda x: x[0], reverse=True)

"""Devuelve una lista de tuplas ordenadas por el promedio de sus dos elementos"""
def ordenar_por_promedio_tiempos(tuplas):
    return sorted(tuplas, key=lambda x: (x[0] + x[1]) / 2)

"""Calcula el tiempo total del analisis de todos los partidos"""
def obtener_tiempo_de_analisis(tuplas):

    tiempo_total_scaloni = 0
    tiempo_total = 0
    tiempo_ayudantes = []

    for s, a in tuplas:
        tiempo_total_scaloni += s
        tiempo_ayudantes.append(tiempo_total_scaloni + a) 
    
    tiempo_total = sorted(tiempo_ayudantes, reverse=True)
    return tiempo_total[0]



def main(n):
    tuplas = [(random.randint(1, 200), random.randint(1, 200)) for _ in range(n)]

    tiempo_con_ordenar_por_mayor_tiempo_ayudantes = obtener_tiempo_de_analisis(ordenar_por_mayor_tiempo_ayudantes(tuplas))
    tiempo_con_ordenar_por_mayor_tiempo_scaloni =  obtener_tiempo_de_analisis(ordenar_por_mayor_tiempo_scaloni(tuplas))
    tiempo_con_ordenar_por_promedio_tiempos = obtener_tiempo_de_analisis(ordenar_por_promedio_tiempos(tuplas))
    tiempo_con_elementos_al_azar =  obtener_tiempo_de_analisis(tuplas)

    print("El tiempo tardado con ordenar_por_mayor_tiempo_ayudantes fue: ", tiempo_con_ordenar_por_mayor_tiempo_ayudantes) #mejor (deberia)

    print("El tiempo tardado con ordenar_por_mayor_tiempo_scaloni fue: ", tiempo_con_ordenar_por_mayor_tiempo_scaloni)

    print("El tiempo tardado con ordenar_por_promedio_tiempos fue: ", tiempo_con_ordenar_por_promedio_tiempos)

    print("El tiempo tardado con tuplas aleatorias fue: ", tiempo_con_elementos_al_azar)

    if (tiempo_con_ordenar_por_mayor_tiempo_ayudantes > tiempo_con_ordenar_por_mayor_tiempo_scaloni or 
        tiempo_con_ordenar_por_mayor_tiempo_ayudantes > tiempo_con_ordenar_por_promedio_tiempos or 
        tiempo_con_ordenar_por_mayor_tiempo_ayudantes > tiempo_con_elementos_al_azar):
        print("SE ENCONTRÓ UN CONTRAEJEMPLO")


main(1000)