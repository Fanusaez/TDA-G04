from TP3.hitting_set_greedy import hitting_set_greedy
from TP3.parser_casos import parsear_archivo


def test_ejemplo_5():
    # k optimo = 2
    _, subconjunto = parsear_archivo('TP3/5.txt')
    assert hitting_set_greedy(subconjunto) == ["Casco", "Colo Barco"]


def test_ejemplo_7():
    # k optimo = 2
    _, subconjunto = parsear_archivo('TP3/7.txt')
    assert hitting_set_greedy(subconjunto) == ["Barcon't", 'Colidio']


def test_ejemplo_10_pocos():
    # k optimo = 3
    _, subconjunto = parsear_archivo('TP3/10_pocos.txt')
    assert hitting_set_greedy(subconjunto) == ['Gallardo', 'Cuti Romero', 'Casco']


def test_ejemplo_10_todos():
    # k optimo = 10
    _, subconjunto = parsear_archivo('TP3/10_todos.txt')
    assert hitting_set_greedy(subconjunto) == ['Dibu', 'Cuti', 'Molina', 'Guido Rodriguez', 'Paredes',
                                                     'Palacios', 'Messi', 'Garnacho', 'Lautaro', 'Perrone']


def test_ejemplo_10_varios():
    # k optimo = 6
    _, subconjunto = parsear_archivo('TP3/10_varios.txt')
    assert hitting_set_greedy(subconjunto) == ["Barcon't", 'Dibu', 'Beltran', 'Riquelme',
                                               'Casco', 'Pezzella', 'Di Maria']


def test_ejemplo_15():
    # k optimo = 4
    _, subconjunto = parsear_archivo('TP3/15.txt')
    assert hitting_set_greedy(subconjunto) == ['Luka Romero', 'Di Maria', 'Colo Barco', 'Dybala', 'Palermo']


def test_ejemplo_20():
    # k optimo = 5
    _, subconjunto = parsear_archivo('TP3/20.txt')
    assert hitting_set_greedy(subconjunto) == ['Riquelme', 'Mauro Zarate', 'El fantasma de la B',
                                               'Ogro Fabianni', "Barcon't"]


def test_ejemplo_50():
    # k optimo = 6
    _, subconjunto = parsear_archivo('TP3/50.txt')
    assert hitting_set_greedy(subconjunto) == ['Tucu Pereyra', 'Casco', 'Dibu', 'Palermo',
                                               "Barcon't", 'Chiquito Romero', 'Burrito Ortega']


def test_ejemplo_75():
    # k optimo = 8
    _, subconjunto = parsear_archivo('TP3/75.txt')
    assert hitting_set_greedy(subconjunto) == ['Gallardo', 'Riquelme', 'Palermo', 'Soule', 'Colo Barco',
                                               'Burrito Ortega', 'Casco', 'Chiquito Romero', 'Buonanotte']


def test_ejemplo_100():
    # k optimo = 9
    _, subconjunto = parsear_archivo('TP3/100.txt')
    assert hitting_set_greedy(subconjunto) == ['Gallardo', 'Langoni', 'Ogro Fabianni', "Barcon't", 'Messi',
                                               'El fantasma de la B', 'Luka Romero', 'Mauro Zarate', 'Soule',
                                               'Di Maria', 'Changuito Zeballos']


def test_ejemplo_200():
    # k optimo = 9
    _, subconjunto = parsear_archivo('TP3/200.txt')
    assert hitting_set_greedy(subconjunto) == ['Gallardo', 'Beltran', 'Luka Romero', 'Mauro Zarate',
                                               'Messi', 'Tucu Pereyra', 'Pity Martinez', 'Pezzella',
                                               'Dibu', 'Palermo']
