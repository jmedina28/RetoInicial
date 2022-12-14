<h1 align="center">Reto Inicial</h1>

---
En este [repositorio](https://github.com/jmedina28/RetoInicial) queda resueltos los ejercicios del Reto Inicial.
***

<h2 align="center">Ejercicio del Caballo</h2>

Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-reinas, el mismo consiste en ubicar n reinas en un tablero de ajedrez de tamaño n x n, sin que las mismas se amenacen. Recuerde que la reina desplaza de manera horizontal, vertical y diagonal como se puede observar en la figura 2, además podemos ver una solución al problema de las 4 reinas. Nótese que una parte importante para resolver un problema es de que manera representar la solución, para este caso particular usamos un vector de n posiciones (columnas) y el valor almacenado representa la fila donde se ubica dicha reina.

![image](https://user-images.githubusercontent.com/91721855/189431913-b1c5e72c-e279-47de-b348-dc41c31146f2.png)
<br>
<img height="500" src="imagenes/1.png" />
<br>

Con esta resolución el código al menos en mi pc me permite ejecutar hasta las combinaciones de 10000 movimientos.

El código empleado para resolverlo es el siguiente:

```python

# Autor: Juan Antonio Pérez Medina
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

x, y, z, j, movimientos, movimiento = [2], [3], [2], [2], int(input("Introduce el número de movimientos que desea que incluya sus combinaciones: ")), 0

# para completar las listas "y" y "z" tenemos que saber que se pueden generar cruzando datos entre ellas.
# Para generar la lista "y" tenemos que saber que cuando el indice de la lista "y" es impar, el siguiente valor de la lista "y" será el doble del anterior
# Cuando el indice sea par, el siguiente valor de la lista "y" vendrá dado por la suma del valor anterior multiplicado por 2 y el valor de la lista "z" en la misma posición.
# Para generar la lista "z" tenemos que saber que cuando el indice de la lista "z" es impar, el siguiente valor de la lista "z" será el doble del anterior
# Cuando el indice sea par, el siguiente valor de la lista "z" vendrá dado por la suma del valor anterior con el valor de la lista "y" en la misma posición.

def recorrer():
    if movimiento < movimientos-2:
        if movimiento % 2 == 0: 
            y.append(y[movimiento]*2), z.append(z[movimiento]*2), x.append(x[movimiento]+y[movimiento]), j.append(y[movimiento+1]) 
        else:
            y.append(y[movimiento]*2 + z[movimiento]), z.append(y[movimiento] + z[movimiento]), x.append(x[movimiento]*2), j.append(j[movimiento]*2) 
        movimiento += 1, recorrer()
    else:
        print(x,y,z,j), print("La cantidad de combinaciones posibles de " + str(movimientos) + " es de " + str(x[-1]*4+y[-1]*2+z[-1]*2+j[-1]))
recorrer()
print(x,y,z,j), print("La cantidad de combinaciones posibles de " + str(movimientos) + " es de " + str(x[-1]*4+y[-1]*2+z[-1]*2+j[-1]))
```
<br>
<img height="500" src="imagenes/IMG_2383.jpg" />
<br>

<h2 align="center">Ejercicio de la Reina</h2>

Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-reinas, el mismo consiste en ubicar n reinas en un tablero de ajedrez de tamaño n x n, sin que las mismas se amenacen. Recuerde que la reina desplaza de manera hori- zontal, vertical y diagonal como se puede observar en la figura 2, además podemos ver una solución al problema de las 4 reinas. Nótese que una parte importante para resolver un problema es de que manera representar la solución, para este caso particular usamos un vector de n posiciones (colum- nas) y el valor almacenado representa la fila donde se ubica dicha reina.

![image](https://user-images.githubusercontent.com/91721855/189432017-53b0d17a-ffad-40e5-b2ae-361dccce7f67.png)

El código empleado para resolverlo es el siguiente:

```python
def teclado(n):
    filasycolumnas = n-1
    tablero = [[]]
    for i in range(filasycolumnas):
        tablero+=[[]]
    for i in tablero:
        for j in range(n):
            i+=[" "]
    return tablero

def desplegartablero(tablero):
    for i in tablero:
        print(i)
    print("____________________________________________________________________")

def calculos():
    n = int(input("¿Cuál es el tamaño del tablero?: "))
    tablero = teclado(n)
    for i in range(0, n):
        for j in range(0, n):
            a = 0 + int(i)
            b = 0 + int(j)
            tablero[i][j] = "r"
            for x in range(0, n):
                if tablero[i][x] != "r":
                    tablero[i][x] = "x"
                if tablero[x][j] != "r":
                    tablero[x][j] = "x"
            if a!=0 and b!=0:
                while a != 0 and b != 0:
                    a-=1
                    b-=1
                    tablero[a][b] = "x"
            a = 0 + int(i)
            b = 0 + int(j)
            while a!=0 or b!=n-1:
                if a!=0 and b!=n-1:
                    a-=1
                    b+=1
                    tablero[a][b] = "x"
                else:
                    break
            a = 0 + int(i)
            b = 0 + int(j)
            if a!=n-1 and b!=n-1:
                while a != n-1 and b != n-1:
                    a+=1
                    b+=1
                    tablero[a][b] = "x"
            a = 0 + int(i)
            b = 0 + int(j)
            while a!=n-1 or b!=0:
                if a!=n-1 and b!=0:
                    a+=1
                    b-=1
                    tablero[a][b] = "x"
                else:
                    break
            desplegartablero(tablero)
            for fila in tablero:
                contador=0
                for z in range(0,n):
                    if fila[z]=="x":
                        contador+=1
                if contador == n:
                    print("No hay solucion")
                    break
            tablero = teclado(n)

calculos()#calcula las casillas que quedarian libres(posibles otras reinas) en un tablero nxn
#tras eso, lo ideal seria repetir la iteracion para buscar otras vez todas las posibles combinaciones
#con la segunda reina, tercera... hasta dar con las soluciones definitivas y contar cuantas hay por tablero
```
