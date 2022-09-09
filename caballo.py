telefono = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
numeros = {
    1: [0,0],
    2: [0,1],
    3: [0,2],
    4: [1,0],
    5: [1,1],
    6: [1,2],
    7: [2,0],
    8: [2,1],
    9: [2,2],
    0: [3,1],
}  

def caballo(movimientos, coords = [], movimientos_totales = 0, iterative = False):
    mov = movimientos
    n = 0

    if movimientos_totales != 0 and iterative == True and coords != []:
        while mov != 0:
            for k in range(8):
                movimiento = mover(coords)
                if movimiento[k][0] >= 0 and movimiento[k][0] <= 2 and movimiento[k][1] >= 0 and movimiento[k][1] <= 2:
                    movimientos_totales += 1
                    iterative = False
                elif movimiento[k] == [3, 1]:
                    movimientos_totales += 1
                    iterative = False
            mov -= 1
        return(movimientos_totales)

    while n < 10 and iterative == False:
        coords = numeros[n]

        for i in range(8):
            movimiento = mover(coords)
            if movimiento[i][0] >= 0 and movimiento[i][0] <= 2 and movimiento[i][1] >= 0 and movimiento[i][1] <= 2:
                movimientos_totales += 1
                if mov > 1:
                    movimientos_totales = caballo(mov - 1, mover(coords)[i], movimientos_totales, True)
            elif movimiento[i] == [3, 1]:
                movimientos_totales += 1
                if mov > 1:
                    movimientos_totales = caballo(mov - 1, mover(coords)[i], movimientos_totales, True)
        n += 1
    print(movimientos_totales)

def mover(coords):
    x = coords[0]
    y = coords[1]
    movimientos_caballo = [[x+2, y+1], [x+2, y-1], [x-2, y+1], [x-2, y-1], [x+1, y+2], [x+1, y-2], [x-1, y+2], [x-1, y-2]]
    return movimientos_caballo


caballo(2)