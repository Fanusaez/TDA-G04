from hitting_set import hitting_set
from parser_casos import parsear_archivo


def test_ejemplo_5():
    universo, subconjunto = parsear_archivo('TP3/5.txt')
    k = 2
    assert hitting_set(universo, subconjunto, k) == ["Barcon't", "Messi"]


def test_ejemplo_7():
    universo, subconjunto = parsear_archivo('TP3/7.txt')
    k = 2
    assert hitting_set(universo, subconjunto, k) == ["Mauro Zarate", "Pezzella"]


def test_ejemplo_10_pocos():
    universo, subconjunto = parsear_archivo('TP3/10_pocos.txt')
    k = 3
    assert hitting_set(universo, subconjunto, k) == ["Chiquito Romero", "Di Maria", "Casco"]


def test_ejemplo_10_todos():
    universo, subconjunto = parsear_archivo('TP3/10_todos.txt')
    k = 10
    assert hitting_set(universo, subconjunto, k) == ['Dibu', 'Cuti', 'Molina', 'Guido Rodriguez', 'Paredes',
                                                     'Palacios', 'Messi', 'Garnacho', 'Lautaro', 'Perrone']

def test_ejemplo_10_varios():
    universo, subconjunto = parsear_archivo('TP3/10_varios.txt')
    k = 6
    assert hitting_set(universo, subconjunto, k) == ['Palermo', 'Dibu', 'Beltran', 'Riquelme', 'Dybala', 'Di Maria']

def test_ejemplo_15():
    universo, subconjunto = parsear_archivo('TP3/15.txt')
    k = 4
    assert hitting_set(universo, subconjunto, k) == ['Chiquito Romero', 'Palermo', 'Luka Romero', 'Dybala']

def test_ejemplo_20():
    universo, subconjunto = parsear_archivo('TP3/20.txt')
    k = 5
    assert hitting_set(universo, subconjunto, k) == ["Barcon't", 'Riquelme', 'El fantasma de la B',
                                                     'Mauro Zarate', 'Ogro Fabianni']

def test_ejemplo_50():
    universo, subconjunto = parsear_archivo('TP3/50.txt')
    k = 10
    assert hitting_set(universo, subconjunto, k) == ["Casco", "Barcon't", "Tucu Pereyra", "Dybala", "Armani", "Langoni"]