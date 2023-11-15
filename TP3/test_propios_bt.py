from hitting_set import hitting_set
from parser_casos import parsear_archivo


def test_ejemplo_5_unico():
    universo, subconjunto = parsear_archivo('sets_generados/5_unico.txt')
    assert hitting_set(universo, subconjunto) == ["Messi"]


def test_ejemplo_5_todos():
    universo, subconjunto = parsear_archivo('sets_generados/5_todos.txt')
    assert hitting_set(universo, subconjunto) == ["Barcon't", "Colo Barco", "Wachoffisde Abila", "Messi", "Cuti Romero"]
