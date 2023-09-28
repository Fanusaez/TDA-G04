from algoritmo import obtener_tiempo_minimo
from parseo_pruebas import obtener_tiempos_de_archivo


def test_caso_con_solo_1_partido():
    s = [1]
    a = [1]
    assert obtener_tiempo_minimo(s, a) == 2
    
def test_caso_con_2_partidos():
    s = [1, 1]
    a = [2, 3]
    assert obtener_tiempo_minimo(s, a) == 4

def test_ejemplo_1_tp():
    s = [60, 50, 70]
    a = [20, 10, 5]
    assert obtener_tiempo_minimo(s, a) == 185

def test_ejemplo_2_tp():
    s = [20, 10, 5]
    a = [60, 50, 70]
    assert obtener_tiempo_minimo(s, a) == 85

def test_ejemplo_catedra_3_elem():
    s, a = obtener_tiempos_de_archivo('textos_pruebas/3_elem.txt')
    assert obtener_tiempo_minimo(s, a) == 10

def test_ejemplo_catedra_10_elem():
    s, a = obtener_tiempos_de_archivo('textos_pruebas/10_elem.txt')
    assert obtener_tiempo_minimo(s, a) == 29

def test_ejemplo_catedra_100_elem():
    s, a = obtener_tiempos_de_archivo('textos_pruebas/100_elem.txt')
    assert obtener_tiempo_minimo(s, a) == 5223

def test_ejemplo_catedra_10000_elem():
    s, a = obtener_tiempos_de_archivo('textos_pruebas/10000_elem.txt')
    assert obtener_tiempo_minimo(s, a) == 497886735
