from parser_casos import parsear_archivo
from programacion_lineal import hitting_set
from hitting_set import es_solucion

def test_ejemplo_5():
    universo, subconjunto = parsear_archivo('TP3/5.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, solucion)
    assert len(solucion) == 2

def test_ejemplo_7():
    universo, subconjunto = parsear_archivo('TP3/7.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 2

def test_ejemplo_10_pocos():
    universo, subconjunto = parsear_archivo('TP3/10_pocos.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 3

def test_ejemplo_10_todos():
    universo, subconjunto = parsear_archivo('TP3/10_todos.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 10

def test_ejemplo_10_varios():
    universo, subconjunto = parsear_archivo('TP3/10_varios.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 6

def test_ejemplo_15():
    universo, subconjunto = parsear_archivo('TP3/15.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 4

def test_ejemplo_20():
    universo, subconjunto = parsear_archivo('TP3/20.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 5

def test_ejemplo_50():
    universo, subconjunto = parsear_archivo('TP3/50.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 6


def test_ejemplo_75():
    universo, subconjunto = parsear_archivo('TP3/75.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 8


def test_ejemplo_100():
    universo, subconjunto = parsear_archivo('TP3/100.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 9


def test_ejemplo_200():
    universo, subconjunto = parsear_archivo('TP3/200.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, hitting_set(universo, subconjunto))
    assert len(solucion) == 9


def test_ejemplo_5_unico():
    universo, subconjunto = parsear_archivo('sets_generados/5_unico.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, solucion)
    assert len(solucion) == 1


def test_ejemplo_5_todos():
    universo, subconjunto = parsear_archivo('sets_generados/5_todos.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, solucion)
    assert len(solucion) == 5

def test_ejemplo_10_unico():
    universo, subconjunto = parsear_archivo('sets_generados/10_unico.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, solucion)
    assert len(solucion) == 1


def test_ejemplo_10_pocos():
    universo, subconjunto = parsear_archivo('sets_generados/10_pocos.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, solucion)
    assert len(solucion) == 2

def test_ejemplo_10_varios():
    universo, subconjunto = parsear_archivo('sets_generados/10_varios.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, solucion)
    assert len(solucion) == 6

def test_ejemplo_15():
    universo, subconjunto = parsear_archivo('sets_generados/15.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, solucion)
    assert len(solucion) == 3


def test_ejemplo_20():
    universo, subconjunto = parsear_archivo('sets_generados/20.txt')
    solucion = hitting_set(universo, subconjunto)
    assert es_solucion(subconjunto, solucion)
    assert len(solucion) == 4
