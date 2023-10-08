import sys
from tp2 import optimo_entrenamientos, obtener_lista_entrenamientos
from parsear_archivo import obtener_energia_demandada_y_disponible

if __name__ == '__main__':
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible(sys.argv[1])
    print("La ganancia máxima es:", optimo_entrenamientos(energia_demandada, energia_disponible))
    print("El plan de entrenamiento es:", obtener_lista_entrenamientos(energia_demandada, energia_disponible))
