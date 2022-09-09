def teclado(n):
    filasycolumnas = n-1
    tablero = [[]]
    for i in range(filasycolumnas):
        tablero+=[[]]
    for i in tablero:
        for j in range(n):
            i+=[" "]
    return tablero

def calculos():
    n = int(input("¿Cuál es el tamaño del teclado?: "))
    tablero = teclado(n)
    for i in range(0, n):
        for j in range(0, n):
            tablero[i][j] = "r"
            for x in range(0, n):
                if tablero[i][x] != "r":
                    tablero[i][x] = "x"
                if tablero[x][i] != "r":
                    tablero[x][i] = "x"
            while i != 0 or j != 0:
                i-=1
                j-=1
                tablero[i][j] = "x"
            while i != n-1 or j != n-1:
                i+=1
                j+=1
                tablero[i][j] = "x"
            print(tablero)
            tablero = teclado(n)

calculos()