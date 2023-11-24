from parser_casos import parsear_archivo
from programacion_lineal import obtener_b, hitting_set, hitting_set_aproximado


def test_5_cota_pl_aproximado():
    universo, subconjunto = parsear_archivo('TP3/5.txt')
    b = obtener_b(subconjunto)
    a_i = len(hitting_set_aproximado(universo, subconjunto))
    z_i = len(hitting_set(universo, subconjunto))
    ratio = a_i / z_i
    print(f"A(I): {a_i}, z(i): {z_i}, ratio: {ratio}, b:{b}")
    assert len(hitting_set(universo, subconjunto)) / len(hitting_set_aproximado(universo, subconjunto)) <= b

def test_7_cota_pl_aproximado():
    universo, subconjunto = parsear_archivo('TP3/7.txt')
    b = obtener_b(subconjunto)
    a_i = len(hitting_set_aproximado(universo, subconjunto))
    z_i = len(hitting_set(universo, subconjunto))
    ratio = a_i / z_i
    print(f"A(I): {a_i}, z(i): {z_i}, ratio: {ratio}, b:{b}")
    assert len(hitting_set(universo, subconjunto)) / len(hitting_set_aproximado(universo, subconjunto)) <= b

def test_15_cota_pl_aproximado():
    universo, subconjunto = parsear_archivo('TP3/15.txt')
    b = obtener_b(subconjunto)
    a_i = len(hitting_set_aproximado(universo, subconjunto))
    z_i = len(hitting_set(universo, subconjunto))
    ratio = a_i / z_i
    print(f"A(I): {a_i}, z(i): {z_i}, ratio: {ratio}, b:{b}")
    assert len(hitting_set(universo, subconjunto)) / len(hitting_set_aproximado(universo, subconjunto)) <= b

def test_20_cota_pl_aproximado():
    universo, subconjunto = parsear_archivo('TP3/20.txt')
    b = obtener_b(subconjunto)
    a_i = len(hitting_set_aproximado(universo, subconjunto))
    z_i = len(hitting_set(universo, subconjunto))
    ratio = a_i / z_i
    print(f"A(I): {a_i}, z(i): {z_i}, ratio: {ratio}, b:{b}")
    assert len(hitting_set(universo, subconjunto)) / len(hitting_set_aproximado(universo, subconjunto)) <= b

def test_50_cota_pl_aproximado():
    universo, subconjunto = parsear_archivo('TP3/50.txt')
    b = obtener_b(subconjunto)
    a_i = len(hitting_set_aproximado(universo, subconjunto))
    z_i = len(hitting_set(universo, subconjunto))
    ratio = a_i / z_i
    print(f"A(I): {a_i}, z(i): {z_i}, ratio: {ratio}, b:{b}")
    assert len(hitting_set(universo, subconjunto)) / len(hitting_set_aproximado(universo, subconjunto)) <= b

def test_75_cota_pl_aproximado():
    universo, subconjunto = parsear_archivo('TP3/75.txt')
    b = obtener_b(subconjunto)
    a_i = len(hitting_set_aproximado(universo, subconjunto))
    z_i = len(hitting_set(universo, subconjunto))
    ratio = a_i / z_i
    print(f"A(I): {a_i}, z(i): {z_i}, ratio: {ratio}, b:{b}")
    assert len(hitting_set(universo, subconjunto)) / len(hitting_set_aproximado(universo, subconjunto)) <= b

def test_100_cota_pl_aproximado():
    universo, subconjunto = parsear_archivo('TP3/100.txt')
    b = obtener_b(subconjunto)
    a_i = len(hitting_set_aproximado(universo, subconjunto))
    z_i = len(hitting_set(universo, subconjunto))
    ratio = a_i / z_i
    print(f"A(I): {a_i}, z(i): {z_i}, ratio: {ratio}, b:{b}")
    assert len(hitting_set(universo, subconjunto)) / len(hitting_set_aproximado(universo, subconjunto)) <= b


def test_200_cota_pl_aproximado():
    universo, subconjunto = parsear_archivo('TP3/200.txt')
    b = obtener_b(subconjunto)
    a_i = len(hitting_set_aproximado(universo, subconjunto))
    z_i = len(hitting_set(universo, subconjunto))
    ratio = a_i / z_i
    print(f"A(I): {a_i}, z(i): {z_i}, ratio: {ratio}, b:{b}")
    assert len(hitting_set(universo, subconjunto)) / len(hitting_set_aproximado(universo, subconjunto)) <= b


