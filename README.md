
Los laberintos se construyen a partir de una clase que se llama "Maze", la cual genera un arreglo de objetos de la clase "Celda"
Además, el método "closeCell" permite cerrar una celda, llamando a su propio método "youCanBeHere(False)", dejándola inaccesible para el "caminante"

El método "checkPath" es el método que lleva a cabo la recursión, en la que se recorre el arreglo hasta que llega al final. 
Cuando llega, empieza un proceso de backtracking en el que se van sumando los números que cuentan las rutas disponibles que se han ido encontrando en las iteraciones anteriores.