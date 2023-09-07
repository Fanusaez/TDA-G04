from algoritmo import obtener_tiempo_minimo


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
