
Los laberintos se construyen a partir de una clase que se llama "Maze", la cual genera un arreglo de objetos de la clase "Celda"
Adem�s, el m�todo "closeCell" permite cerrar una celda, llamando a su propio m�todo "youCanBeHere(False)", dej�ndola inaccesible para el "caminante"

El m�todo "checkPath" es el m�todo que lleva a cabo la recursi�n, en la que se recorre el arreglo hasta que llega al final. 
Cuando llega, empieza un proceso de backtracking en el que se van sumando los n�meros que cuentan las rutas disponibles que se han ido encontrando en las iteraciones anteriores.