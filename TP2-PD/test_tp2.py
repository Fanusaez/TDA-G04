import pytest

from parsear_archivo import obtener_energia_demandada_y_disponible, obtener_resultado
from tp2 import optimo_entrenamientos, obtener_lista_entrenamientos


# Tests catedra optimo valor entrenado
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

@pytest.mark.timeout(60)
def test_5000_elementos():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/5000.txt')
    assert optimo_entrenamientos(energia_demandada, energia_disponible) == 279175

# Tests catedra optimo lista entrenamientos

def test_3_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/3.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['3.txt'][1]

def test_10_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/10.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['10.txt'][1]

def test_10_bis_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/10_bis.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['10_bis.txt'][1]

def test_10_todo_entreno_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/10_todo_entreno.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['10_todo_entreno.txt'][1]

def test_50_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/50.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['50.txt'][1]

def test_50_bis_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/50_bis.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['50_bis.txt'][1]

def test_100_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/100.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['100.txt'][1]

def test_500_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/500.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['500.txt'][1]

def test_1000_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/1000.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['1000.txt'][1]

@pytest.mark.timeout(60)
def test_5000_elementos_lista():
    energia_demandada, energia_disponible = obtener_energia_demandada_y_disponible('textos_pruebas/5000.txt')
    resultados = obtener_resultado('textos_pruebas/Resultados Esperados.txt')

    assert obtener_lista_entrenamientos(energia_demandada, energia_disponible) == resultados['5000.txt'][1]
