from TP3.hitting_set_greedy import hitting_set_greedy
from TP3.parser_casos import parsear_archivo


def test_ejemplo_5():
    universo, subconjunto = parsear_archivo('TP3/5.txt')
    k = 2
    assert hitting_set_greedy(universo, subconjunto, k) == ["Casco", "Cuti Romero"]


def test_ejemplo_7():
    universo, subconjunto = parsear_archivo('TP3/7.txt')
    k = 2
    assert hitting_set_greedy(universo, subconjunto, k) == ["Mauro Zarate", "Pezzella"]


