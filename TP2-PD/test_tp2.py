from parsear_archivo import obtener_energia_demandada_y_disponible
from tp2 import optimo_entrenamientos

def test_3_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/3.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 7


def test_10_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/10.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 380

def test_10_bis_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/10_bis.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 523

def test_10_todo_entreno():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/10_todo_entreno.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 900

def test_50_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/50.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 1870

def test_50_bis_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/50_bis.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 2136

def test_100_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/100.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 5325

def test_500_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/500.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 27158

def test_1000_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/1000.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 54021

def test_5000_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/5000.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 279125
