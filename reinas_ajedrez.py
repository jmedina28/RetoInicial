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