lista= [[6,8],[7,9][4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4],[4,6]]
movimientos=[]

def movimientos(inicio, recorrido):
    n = 0
    if recorrido:
        for i in lista[inicio]:
            movimiento += 1 + movimientos(n, recorrido - 1)
    return movimiento





