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
            print(tablero)
            tablero = teclado(n)

calculos()