from TP3.hitting_set_greedy import hitting_set_greedy
from TP3.parser_casos import parsear_archivo


def test_ejemplo_5():
    _, subconjunto = parsear_archivo('TP3/5.txt')
    assert hitting_set_greedy(subconjunto) == ["Casco", "Cuti Romero"]


def test_ejemplo_7():
    _, subconjunto = parsear_archivo('TP3/7.txt')
    assert hitting_set_greedy(subconjunto) == ["Mauro Zarate", "Pezzella"]


