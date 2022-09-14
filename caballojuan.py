# Autor: Juan Antonio Pérez Medina.

x, y, z, j, movimientos, movimiento = [2], [3], [2], [2], int(input("Introduce el número de movimientos que desea que incluya sus combinaciones: ")), 0

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
