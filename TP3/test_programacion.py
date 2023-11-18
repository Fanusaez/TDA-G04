from programacion_lineal import hitting_set
from parser_casos import parsear_archivo

def test_ejemplo_5():
    universo, subconjunto = parsear_archivo('TP3/5.txt')
    assert hitting_set(universo, subconjunto) == ["Barcon't", "Messi"]


def test_ejemplo_7():
    universo, subconjunto = parsear_archivo('TP3/7.txt')
    assert hitting_set(universo, subconjunto) == ["Mauro Zarate", "Pezzella"]


def test_ejemplo_10_pocos():
    universo, subconjunto = parsear_archivo('TP3/10_pocos.txt')
    assert hitting_set(universo, subconjunto) == ["Chiquito Romero", "Di Maria", "Casco"]


def test_ejemplo_10_todos():
    universo, subconjunto = parsear_archivo('TP3/10_todos.txt')
    assert len(hitting_set(universo, subconjunto)) == len(['Dibu', 'Cuti', 'Molina', 'Guido Rodriguez', 'Paredes',
                                                     'Palacios', 'Messi', 'Garnacho', 'Lautaro', 'Perrone'])
