from algoritmo import obtener_tiempo_minimo
from parseo_pruebas import obtener_tiempos_de_archivo


def test_caso_con_solo_1_partido():
    s = [1]
    a = [1]
    assert obtener_tiempo_minimo(1, s, a) == 2
    
def test_caso_con_2_partidos():
    # S  # 1 2 3 4 5 6 7 8 9
    # A1 # s s
    # A2 # - a a a
    # A3 # - - a a 
    s = [1, 1]
    a = [2, 3]
    assert obtener_tiempo_minimo(2, s, a) == 4

def test_caso_1_ejemplo_catedra_3_elem():
    # Dado el path: textos_pruebas/3_elem.txt

    s, a = obtener_tiempos_de_archivo('./textos_pruebas/3_elem.txt')
    assert obtener_tiempo_minimo(3, s, a) == 10

def test_caso_2_ejemplo_catedra_10_elem():
    # Dado el path: textos_pruebas/10_elem.txt

    s, a = obtener_tiempos_de_archivo('./textos_pruebas/10_elem.txt')
    assert obtener_tiempo_minimo(10, s, a) == 29

def test_caso_3_ejemplo_catedra_100_elem():
    # Dado el path: textos_pruebas/100_elem.txt

    s, a = obtener_tiempos_de_archivo('./textos_pruebas/100_elem.txt')
    assert obtener_tiempo_minimo(100, s, a) == 5223

def test_caso_4_ejemplo_catedra_10000_elem():
    # Dado el path: textos_pruebas/10000_elem.txt

    s, a = obtener_tiempos_de_archivo('./textos_pruebas/10000_elem.txt')
    assert obtener_tiempo_minimo(10000, s, a) == 497886735
