import sys
from parser_casos import parsear_archivo
from hitting_set import hitting_set as hitting_set_bt
from programacion_lineal import hitting_set as hitting_set_pl
from programacion_lineal import hitting_set_aproximado as hitting_set_plc
from hitting_set_greedy import hitting_set_greedy


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error en la cantidad de argumentos")
        exit(1)

    universo, subconjuntos = parsear_archivo(sys.argv[1])

    if sys.argv[2] == "bt":
            solucion =  hitting_set_bt(universo, subconjuntos)
            print(f"La solucion con backtracking es: {solucion}")
    elif sys.argv[2] == "pl":
            solucion = hitting_set_pl(universo, subconjuntos)
            print(f"La solucion con programacion lineal es: {solucion}")
    elif sys.argv[2] == "plc":
            solucion = hitting_set_plc(universo, subconjuntos)
            print(f"La solucion con programacion lineal continua es: {solucion}")
    elif sys.argv[2] == "gdy":
            solucion = hitting_set_greedy(universo, subconjuntos)
            print(f"La solucion con greedy es: {solucion}")
    else:
        print("Error en el argumento de algoritmo")
        exit(1)
