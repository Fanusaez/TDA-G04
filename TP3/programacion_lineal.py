from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, lpSum, PULP_CBC_CMD

from parser_casos import parsear_archivo


def hitting_set(universo, subconjuntos):
    # Define el problema de optimización
    prob = LpProblem("HittingSet", LpMinimize)

    # Crea variables binarias para cada elemento en el conjunto universo
    x_vars = LpVariable.dicts("x", universo, cat='Binary')
    # print(x_vars)

    # Funcion objetivo: suma de todas las x_i
    prob += lpSum(x_vars[i] for i in universo)

    # Restricciones: cada subconjunto debe tener al menos un elemento seleccionado
    for subset in subconjuntos:
        prob += lpSum(x_vars[i] for i in subset if i in universo) >= 1

    # Resolver el problema
    prob.solve(PULP_CBC_CMD(msg=False))

    # Revisar si la solución es óptima y devolver el resultado
    if LpStatus[prob.status] == 'Optimal':
        # Devuelve los elementos seleccionados para el hitting set
        return [i for i in universo if x_vars[i].value() == 1]
    return None

def hitting_set_aproximado(universo, subconjuntos):
    """
    """
    # Hago que no se impriman los mensajes de pulp
    prob = LpProblem("HittingSet", LpMinimize)

    # Crea variables continuas para cada elemento en el conjunto universo
    x_vars = LpVariable.dicts("x", universo, lowBound=0, upBound=1)
    #print(x_vars)

    # Funcion objetivo: suma de todas las x_i
    prob += lpSum(x_vars[i] for i in universo)

    # Restricciones: cada subconjunto debe tener al menos un elemento seleccionado
    for subset in subconjuntos:
        prob += lpSum(x_vars[i] for i in subset if i in universo) >= 1

    # Resolver el problema
    prob.solve(PULP_CBC_CMD(msg=False))

    #print("Status:", LpStatus[prob.status])
    #print("")
    #print("Solucion:")
    #for v in prob.variables():
    #   print(v.name, "=", v.varValue)
    b = obtener_b(subconjuntos)
    if LpStatus[prob.status] == 'Optimal':
        # Imprimo la solucion previo al redondeo
        #print("Solucion previo al redondeo:")
        #for v in prob.variables():
            #print(v.name, "=", v.varValue)
        #print("b = ", b)

        # Devuelve los elementos seleccionados para el hitting set
        return [i for i in universo if x_vars[i].value() >= 1/b]

    # Aca deberia devolver el universo
    return None


def obtener_b(subconjuntos):
    return max([len(subset) for subset in subconjuntos])


def main():
    universo, subconjunto = parsear_archivo('sets-catedra/100.txt')
    solucion = hitting_set_aproximado(universo, subconjunto)
    #print(solucion)
    #print("k = ", len(solucion))

if __name__ == '__main__':
    main()
