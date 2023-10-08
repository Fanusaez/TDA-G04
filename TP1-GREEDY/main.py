import sys
from algoritmo import obtener_tiempo_minimo
from parseo_pruebas import obtener_tiempos_de_archivo

if __name__ == '__main__':
    s, a = obtener_tiempos_de_archivo(sys.argv[1])
    print("El tiempo optimo es:", obtener_tiempo_minimo(s, a))
