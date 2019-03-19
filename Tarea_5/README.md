														-----[Tarea Dynamic Programming]-----
Objetivo: Emplear DP con la finalidad de optimizar nuestros algoritmos. Lo que busca DP es no gastar recursos en hacer operaciones innecesarias o repetir acciones que ya hicimos. Esto lo hacemos por medio de re-utilizar resultados que obtuvimos en operaciones previas.

Ejercicios:
	1.- Crear un algoritmo que encuentre el n�mero de subsets que sumen una cantidad dada, dentro de un set de enteros dados.
	2.- Crear un algoritmos que encuentre el numero de caminos que una gallina que solo puede moverse hacia abajo y a la derecha tiene para llegar a un punto final dado.

Explicaciones:
	Los laberintos se construyen a partir de una clase que se llama "Maze", la cual genera un arreglo de objetos de la clase "Celda"
	Adem�s, el m�todo "closeCell" permite cerrar una celda, llamando a su propio m�todo "youCanBeHere(False)", dej�ndola inaccesible para el "caminante"

	El m�todo "checkPath" es el m�todo que lleva a cabo la recursi�n, en la que se recorre el arreglo hasta que llega al final. 
	Cuando llega, empieza un proceso de backtracking en el que se van sumando los n�meros que cuentan las rutas disponibles que se han ido encontrando en las iteraciones anteriores.