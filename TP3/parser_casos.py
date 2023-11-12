def parsear_archivo(path):
    # Dado un path, parsea el archivo que tiene el formato csv
    # y devuelve una lista de listas con los datos
    # Tambien devuelve una lista con todos los valores unicos de la lista

    with open(path) as archivo:
        lineas = archivo.readlines()
        datos = []
        for linea in lineas:
            datos.append(linea.strip().split(','))

    valores_unicos = []
    for fila in datos:
        for valor in fila:
            if valor not in valores_unicos:
                valores_unicos.append(valor)

    return valores_unicos, datos
