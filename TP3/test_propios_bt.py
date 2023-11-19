from hitting_set import hitting_set
from parser_casos import parsear_archivo


def test_ejemplo_5_unico():
    universo, subconjunto = parsear_archivo('sets_generados/5_unico.txt')
    assert hitting_set(universo, subconjunto) == ["Messi"]


def test_ejemplo_5_todos():
    universo, subconjunto = parsear_archivo('sets_generados/5_todos.txt')
    assert hitting_set(universo, subconjunto) == ["Barcon't", "Colo Barco", "Wachoffisde Abila", "Messi", "Cuti Romero"]


def test_ejemplo_10_unico():
    universo, subconjunto = parsear_archivo('sets_generados/10_unico.txt')
    assert hitting_set(universo, subconjunto) == ["Dibu"]


def test_ejemplo_10_pocos():
    universo, subconjunto = parsear_archivo('sets_generados/10_pocos.txt')
    assert hitting_set(universo, subconjunto) == ["Messi", "Di Maria"]


def test_ejemplo_10_varios():
    universo, subconjunto = parsear_archivo('sets_generados/10_varios.txt')
    assert hitting_set(universo, subconjunto) == ['Di Maria', 'Colo Barco', 'Tagliafico',
                                                  'Martinez', 'Alvarez', 'Perez']


def test_ejemplo_15():
    universo, subconjunto = parsear_archivo('sets_generados/15.txt')
    assert hitting_set(universo, subconjunto) == ["Alvarez", "Fernandez",  "Dibu"]


def test_ejemplo_20():
    universo, subconjunto = parsear_archivo('sets_generados/20.txt')
    assert hitting_set(universo, subconjunto) == ["Alvarez", "Fernandez", "Dibu", "Palacios"]

