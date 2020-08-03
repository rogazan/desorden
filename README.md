# Listas con grado de desorden controlado
Genera distintos grados de desorden en una lista inicialmente ordenada. Se propone una clase “desorden” que se instancia con el número de elementos que se necesitan en la lista. La instancia dispone de una lista inicialmente ordenada de enteros en el atributo “.datos” de la instancia, al que se le pueden aplicar transformaciones sucesivas con los métodos descritos a continuación


# Generar instancia de la clase "desorden"

	lista = desorden(20)

	print(lista)

	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

La clase dispone de una serie de métodos para generar distintos grados de entropía en la lista. Todos los métodos se pueden aplicar a la lista completa o a un rango de la misma:


# Método .invertir

desorden.invertir ([inicio[, fin]])

Invierte los valores de la lista en su totalidad o en el rango definido por los argumentos inicio, fin.

	lista = desorden(20)

	# Invierte la lista completa

	lista.invertir()

	print(lista)

	[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



	lista = desorden(20)
	
	# Invierte el rango 5-10

	lista.invertir(5, 10)

	print(lista)

	[0, 1, 2, 3, 4, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 15, 16, 17, 18, 19]



	lista = desorden(20)
	
	# Invierte el rango entre el elemento 5 y el final de la lista

	lista.invertir(5)

	print(lista)

	[0, 1, 2, 3, 4, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]

# Metodo .barajar

desorden.barajar ([inicio [, fin]])

Aplica el método shuffle  a la lista en su totalidad o al rango definido por los argumentos inicio, fin.

	lista = desorden(20)

	# Baraja todos los elementos en el rango 5-10
	
	lista.barajar(5, 10)

	print(lista)

	[0, 1, 2, 3, 4, 6, 9, 12, 11, 8, 14, 10, 5, 13, 7, 15, 16, 17, 18, 19]


# Método .repetir

desorden.repetir(elementos=1, [inicio [, fin]])

Extrae el número de valores indicado por <elementos> (1 por defecto) de la lista completa o del  rango especificado y los repite aleatoriamente en ese mismo rango.

	lista = desorden(20)
	
	# Extrae 3 elementos al azar del rango 5-10 y los distribuye aleatoriamente en el mismo rango
	
	lista.repetir(3, 5, 10)
	
	print(lista)
	
	[0, 1, 2, 3, 4, 13, 14, 10, 13, 13, 10, 14, 13, 14, 10, 15, 16, 17, 18, 19]


# Método cambiar

desorden.cambiar(pct=0.1, [inicio [, fin]])

Intercambia una tasa  <pct>  (por defecto 0,1) de elementos de la lista completa o del rango especificado

	lista = desorden(20)

	# Intercambia el 50% de los elementos del rango 5 a 15
	
	lista.cambiar(0.5, 5, 10)  # Intercambia el 50% de los elementos del rango 5 a 15

	print(lista)
	
	[0, 1, 2, 3, 4, 5, 10, 7, 8, 9, 13, 6, 12, 11, 14, 15, 16, 17, 18, 19]D


# Método rotar

desorden.rotar(unidades= 1, [inicio [, fin]])

Rota circularmente los elementos de la lista o del rango especificado con un desplazamiento de <unidades>

	lista = desorden(20)
	
	# Intercambia el 50% de los elementos del rango 5 a 15
	
	lista.rotar(2, 5, 10)  # Rota dos posiciones los elementos del rango 5-10

	print(lista)

	[0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 5, 6, 15, 16, 17, 18, 19]


# Método ordenar

desorden.ordenar([inicio [, fin]])

Ordena la lista o el rango especificado utilizando el método sort de python

	lista = desorden(20)

	# ordena el rango 5-15

	lista.ordenar(5, 15)  

	print(lista)

	[9, 8, 14, 0, 15, 1, 2, 3, 5, 6, 7, 10, 13, 16, 17, 12, 18, 11, 19, 4]
