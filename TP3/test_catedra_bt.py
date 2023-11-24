import pytest

from hitting_set import hitting_set
from parser_casos import parsear_archivo


def test_ejemplo_5():
    universo, subconjunto = parsear_archivo('sets-catedra/5.txt')
    assert hitting_set(universo, subconjunto) == ["Barcon't", "Messi"]


def test_ejemplo_7():
    universo, subconjunto = parsear_archivo('sets-catedra/7.txt')
    assert hitting_set(universo, subconjunto) == ["Mauro Zarate", "Pezzella"]


def test_ejemplo_10_pocos():
    universo, subconjunto = parsear_archivo('sets-catedra/10_pocos.txt')
    assert hitting_set(universo, subconjunto) == ["Chiquito Romero", "Di Maria", "Casco"]

@pytest.mark.skip(reason="No se puede resolver en tiempo razonable")

def test_ejemplo_10_todos():
    universo, subconjunto = parsear_archivo('sets-catedra/10_todos.txt')
    assert hitting_set(universo, subconjunto) == ['Dibu', 'Cuti', 'Molina', 'Guido Rodriguez', 'Paredes',
                                                  'Palacios', 'Messi', 'Garnacho', 'Lautaro', 'Perrone']

@pytest.mark.skip(reason="No se puede resolver en tiempo razonable")

def test_ejemplo_10_varios():
    universo, subconjunto = parsear_archivo('sets-catedra/10_varios.txt')
    assert hitting_set(universo, subconjunto) == ['Palermo', 'Dibu', 'Beltran', 'Riquelme', 'Dybala',
                                                  'Di Maria']

@pytest.mark.skip(reason="No se puede resolver en tiempo razonable")

def test_ejemplo_15():
    universo, subconjunto = parsear_archivo('sets-catedra/15.txt')
    assert hitting_set(universo, subconjunto) == ['Chiquito Romero', 'Palermo', 'Luka Romero', 'Dybala']

@pytest.mark.skip(reason="No se puede resolver en tiempo razonable")

def test_ejemplo_20():
    universo, subconjunto = parsear_archivo('sets-catedra/20.txt')
    assert hitting_set(universo, subconjunto) == ["Barcon't", 'Riquelme', 'El fantasma de la B',
                                                  'Mauro Zarate', 'Ogro Fabianni']

@pytest.mark.skip(reason="No se puede resolver en tiempo razonable")

def test_ejemplo_50():
    universo, subconjunto = parsear_archivo('sets-catedra/50.txt')
    assert hitting_set(universo, subconjunto) == ["Casco", "Barcon't", "Tucu Pereyra",
                                                  "Dybala", "Armani", "Langoni"]

@pytest.mark.skip(reason="No se puede resolver en tiempo razonable")
def test_ejemplo_75():
    universo, subconjunto = parsear_archivo('sets-catedra/75.txt')
    assert hitting_set(universo, subconjunto) == ['Simeone', 'Riquelme', 'Casco', 'Palermo', 'Chiquito Romero',
                                                  'Ogro Fabianni', 'Cuti Romero', 'Beltran']

@pytest.mark.skip(reason="No se puede resolver en tiempo razonable")
def test_ejemplo_100():
    universo, subconjunto = parsear_archivo('sets-catedra/100.txt')
    assert hitting_set(universo, subconjunto) == ["Barcon't", 'Armani', 'Gallardo', 'Langoni', 'El fantasma de la B',
                                                  'Soule', 'Wachoffisde Abila', 'Messi', 'Changuito Zeballos']

@pytest.mark.skip(reason="No se puede resolver en tiempo razonable")
def test_ejemplo_200():
    universo, subconjunto = parsear_archivo('sets-catedra/200.txt')
    assert hitting_set(universo, subconjunto) == ['Mauro Zarate', 'Tucu Pereyra', 'Beltran', 'Gallardo', 'Pity Martinez',
                                                  "Barcon't", 'Palermo', 'Soule', 'Chiquito Romero']

