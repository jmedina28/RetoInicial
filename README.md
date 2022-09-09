<h1 align="center">Reto Inicial</h1>

---
En este [repositorio](https://github.com/jmedina28/RetoInicial) queda resueltos los ejercicios del Reto Inicial.
***

<h2 align="center">Ejercicio del Caballo</h2>

Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-reinas, el mismo consiste en ubicar n reinas en un tablero de ajedrez de tamaño n x n, sin que las mismas se amenacen. Recuerde que la reina desplaza de manera horizontal, vertical y diagonal como se puede observar en la figura 2, además podemos ver una solución al problema de las 4 reinas. Nótese que una parte importante para resolver un problema es de que manera representar la solución, para este caso particular usamos un vector de n posiciones (columnas) y el valor almacenado representa la fila donde se ubica dicha reina.

![image](https://user-images.githubusercontent.com/91721855/189431913-b1c5e72c-e279-47de-b348-dc41c31146f2.png)


El código empleado para resolverlo es el siguiente:

```python

posibilidad = []
diccionario= {
        1: [8,6],
        2: [7,9],
        3: [4,8],
        4: [9,3,0],
        5: [],
        6: [7,1,0],
        7: [6,2],
        8: [1,3],
        9: [2,4],
        0: [4,6]
    }

casilla = 1

def recorrer1():
    posibilidad1 = []

    
    for i in range(len(diccionario[casilla])):
        posicion = i
        posibilidad1.append(diccionario[casilla][posicion])
    print(posibilidad1)
    posibilidades_unicas = []
    for o in posibilidad1:
        if o not in posibilidades_unicas:
            posibilidades_unicas.append(o)

    print(posibilidades_unicas)
    
    for n in range(len(posibilidades_unicas)):
        posibilidad1.extend(diccionario[posibilidades_unicas[n]])
        
    print(posibilidad1)
    for o in posibilidad1:
        if o not in posibilidades_unicas:
            posibilidades_unicas.append(o)
    print(posibilidades_unicas)

    print(len(posibilidad1)-len(diccionario[casilla]))
    
recorrer1()
```

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
