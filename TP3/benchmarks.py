from hitting_set import hitting_set as hitting_set_backtracking
from parser_casos import parsear_archivo
from programacion_lineal import hitting_set as hitting_set_programacion_lineal_entera
from programacion_lineal import hitting_set_aproximado as hitting_set_programacion_lineal_continua
from hitting_set_greedy import hitting_set_greedy as hitting_set_greedy

import time

def benchmark_algoritmos():
    # Archivos de casos de test
    archivos = [
        "5.txt",
        "7.txt",
        "10_pocos.txt",
        "10_todos.txt",
        "10_varios.txt",
        "15.txt",
        "20.txt",
        "50.txt",
        "75.txt",
        "100.txt",
        "200.txt",
    ]

    # Algoritmos a probar
    algoritmos = [
        # hitting_set_backtracking,
        hitting_set_programacion_lineal_entera,
        hitting_set_programacion_lineal_continua,
        hitting_set_greedy,
    ]

    # Ejecuta los algoritmos para cada archivo
    for archivo in archivos:
        print("Archivo:", archivo)
        print("lineal_entera | lineal_continua | greedy")
        universo, subconjuntos = parsear_archivo("TP3/" + archivo)

        # Inicia la medición de tiempos para cada algoritmo
        tiempos = []
        for algoritmo in algoritmos:
            inicio = time.time()
            algoritmo(universo, subconjuntos)
            fin = time.time()
            tiempos.append(fin - inicio)

        # Imprime los tiempos de ejecución de cada algoritmo
        print(" | ".join([f"{t:.5f}s" for t in tiempos]))
        # Imprimo el largo de la solucion
        print(" | ".join([str(len(algoritmo(universo, subconjuntos))) for algoritmo in algoritmos]))
        print("")

def main():
    benchmark_algoritmos()

if __name__ == "__main__":
    main()