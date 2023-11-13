from hitting_set import hitting_set
from parser_casos import parsear_archivo


def test_ejemplo_5():
    universo, subconjunto = parsear_archivo('TP3/5.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 2


def test_ejemplo_7():
    universo, subconjunto = parsear_archivo('TP3/7.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 2


def test_ejemplo_10_pocos():
    universo, subconjunto = parsear_archivo('TP3/10_pocos.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 3


def test_ejemplo_10_todos():
    universo, subconjunto = parsear_archivo('TP3/10_todos.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 10


def test_ejemplo_10_varios():
    universo, subconjunto = parsear_archivo('TP3/10_varios.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 6


def test_ejemplo_15():
    universo, subconjunto = parsear_archivo('TP3/15.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 4


def test_ejemplo_20():
    universo, subconjunto = parsear_archivo('TP3/20.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 5


def test_ejemplo_50():
    universo, subconjunto = parsear_archivo('TP3/50.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 6


def test_ejemplo_75():
    universo, subconjunto = parsear_archivo('TP3/75.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 8


def test_ejemplo_100():
    universo, subconjunto = parsear_archivo('TP3/100.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 9


def test_ejemplo_200():
    universo, subconjunto = parsear_archivo('TP3/200.txt')
    k = 11
    assert len(hitting_set(universo, subconjunto, k)) == 9

