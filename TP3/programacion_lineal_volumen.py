from programacion_lineal import hitting_set as hitting_set_programacion_lineal_entera
from parser_casos import parsear_archivo

import time

def benchmark_pl():
    # Archivos de casos de test
    archivos = [
        "1000.txt"
    ]

    # Ejecuta los algoritmos para cada archivo
    for archivo in archivos:
        print("Archivo:", archivo)
        universo, subconjuntos = parsear_archivo("sets_randomizados_volumen/" + archivo)

        # Inicia la medición de tiempos para cada algoritmo
        inicio = time.time()
        solucion = hitting_set_programacion_lineal_entera(universo, subconjuntos)
        fin = time.time()
        tiempo = fin - inicio

        # Imprime los tiempos de ejecución de cada algoritmo
        print(f"{tiempo:.5f}s")
        # Imprimo el largo de la solucion
        print(len(solucion))
        print("")


def main():
    benchmark_pl()

if __name__ == "__main__":
    main()