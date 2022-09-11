# Gracias al código de prueba que realicé ayer, pude ver de mejor forma el patrón que existía en el tablero y la cantidad de 
# n movimientos que se podían realizar desde cada una de las casillas.
# Asi que considero que este código es mucho más eficiente que el anterior y que practicamente cualquiera que se pueda obtener para la resolución de este problema.

# Como podemos ver a lo largo de la ejecución del otro código hay variables que se comportan de forma parecida.
# Por ejemplo, las cuatro esquinas del tablero (1,3,7,9) sea par o impar la cantidad de movimientos que se pueden realizar desde 
# cada una de ellas son coincidentes en cuanto a combinaciones se refiere asi que podemos llamar a esa variable "x"
# Lo mismo ocurre con el 2 y el 8 que van a ser nuestra variable "z" y con el 4 y el 6 que van a ser nuestra variable "y"
# El 5 siempre es nulo y el 0 será nuestra variable "j"
"""
Podemos realizar una serie de observaciones:
    1. Cuando el numero de movimientos es par la variable "y" se iguala con la "j"
    2. Cuando el numero de movimientos es impar la variable "x" se iguala con la "z" dejando las filas 1 y 3 con los mismos valores.

"""
# Aun así parece que no es suficiente para poder hallar una solución pero combinando la la información obtenida en el código de prueba
# con un poco de trabajo a papel y boli, he podido llegar a la conclusion que vendrá dada en formato imagen después de esta solución.

# Las listas que voy a crear van a ser las series de n cantidad de combinaciones posibles para i movimientos correspondientes a cada una de las casillas del tablero.
x = [2]
y = [3]
z = [2]
j = [2]
