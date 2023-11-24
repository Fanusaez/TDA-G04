
# universo de jugadores
jugadores_argentinos = [ "Lionel Messi", "Diego Maradona", "Juan Roman Riquelme", "Gabriel Batistuta", "Alfredo Di Stefano",
                         "Javier Zanetti", "Mario Kempes", "Fernando Redondo", "Daniel Passarella", "Javier Mascherano", "Gonzalo Higuain",
                         "Ariel Ortega", "Claudio Caniggia", "Esteban Cambiasso", "Ezequiel Lavezzi", "Hernan Crespo", "Sergio Aguero",
                         "Roberto Ayala", "Jorge Valdano", "Carlos Tevez", "Juan Sebastian Veron", "Oscar Ruggeri", "Pablo Aimar",
                         "Juan Pablo Sorin", "Walter Samuel", "Nicolas Burdisso", "Maxi Rodriguez", "Martin Palermo", "Jose Luis Brown",
                         "Americo Gallego", "German Burgos", "Claudio Lopez", "Diego Simeone", "Emiliano Martinez", "Nicolas Otamendi",
                         "Leandro Paredes", "Federico Valverde", "Angel Di Maria", "Paulo Dybala", "Mauro Icardi", "Giovani Lo Celso",
                         "Marcos Rojo", "Guido Rodriguez", "Rodrigo De Paul", "Lucas Ocampos", "Nahuel Guzman", "Eduardo Salvio",
                         "Fabricio Coloccini", "Juan Foyth", "Roberto Pereyra", "Javier Pastore", "Lucas Biglia", "Ezequiel Garay",
                         "Fernando Gago", "Pablo Zabaleta", "Erik Lamela", "Santiago Solari", "Juan Iturbe", "Diego Milito",
                         "Fernando Cavenaghi", "Andres Guglielminpietro", "Pablo Sorin", "Claudio Yacob", "Juan Pablo Angel",
                         "Rene Higuita", "Matias Almeyda", "Javier Pastore", "Eduardo Vargas", "Pablo Daniel Osvaldo", "Eduardo Tuzzio",
                         "Sergio Romero", "Nestor Sensini", "Mauro Camoranesi", "Juan Roman Riquelme", "Claudio Caniggia", "Santiago Ascacibar",
                         "Fernando Belluschi", "Angel Correa", "Carlos Bilardo", "Sergio Goycochea", "Juan Manuel Iturbe", "Mariano Andujar",
                         "Roberto Sensini", "Ramiro Funes Mori", "Eduardo Coudet", "Lucas Pratto", "Juan Mercier", "Mauro Boselli",
                         "Enzo Francescoli", "Sebastian Battaglia", "Lucas Barrios", "Leonardo Ponzio"]

# generar un txt eligiendo al azar un numero x de jugadores de la lista de jugadores_argentinos en cada rengon
# el numero x de jugadores se elige al azar entre 5 y 20

import random
def generar_txt(cant_subconjuntos):
    #abrir archivo para escribir
    nombre_archivo = "sets_randomizados_volumen/%s.txt" % cant_subconjuntos
    archivo = open(nombre_archivo, "w")
    for _ in range(cant_subconjuntos):

        #elijo un numero al azar entre 5 y 20
        cant_jugadores = random.randint(5,10)

        #elijo al azar los jugadores
        jugadores = random.sample(jugadores_argentinos, cant_jugadores)

        #escribo en el archivo con formato jugador1,jugador2,jugador3
        for jugador in jugadores:

            #si es el ultimo jugador no escribo la coma
            if jugador == jugadores[-1]:
                archivo.write(jugador)
            else:
                archivo.write(jugador + ",")
        archivo.write("\n")
    archivo.close()

