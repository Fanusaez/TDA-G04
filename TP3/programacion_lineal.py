from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, lpSum

def hitting_set(universo, subconjuntos):
    # Define el problema de optimización
    prob = LpProblem("HittingSet", LpMinimize)

    # Crea variables binarias para cada elemento en el conjunto universo
    x_vars = LpVariable.dicts("x", universo, cat='Binary')
    print(x_vars)

    # Funcion objetivo: suma de todas las x_i
    prob += lpSum(x_vars[i] for i in universo)

    # Restricciones: cada subconjunto debe tener al menos un elemento seleccionado
    for subset in subconjuntos:
        prob += lpSum(x_vars[i] for i in subset if i in universo) >= 1

    # Resolver el problema
    prob.solve()

    # Revisar si la solución es óptima y devolver el resultado
    if LpStatus[prob.status] == 'Optimal':
        # Devuelve los elementos seleccionados para el hitting set
        return [i for i in universo if x_vars[i].value() == 1]
    return None

def main():
    # Ejemplo de uso:
    universo = ['A', 'B', 'C', 'D', 'F']
    subconjuntos = [['A', 'B'], ['B', 'C'], ['B', 'D'], ['D', 'F']]

    # Llama a la función con el ejemplo dado
    hitting_set_result = hitting_set(universo, subconjuntos)
    print(hitting_set_result)

if __name__ == '__main__':
    main()
