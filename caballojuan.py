# Autor: Juan Antonio Pérez Medina.

x, y, z, j, movimientos = [2], [3], [2], [2], int(input("Introduce el número de movimientos que desea que incluya sus combinaciones: "))

def recorrer(nmov):

    for i in range(nmov-1):
        if i % 2 == 0: 
            y.append(y[i]*2), z.append(z[i]*2), x.append(x[i]+y[i]), j.append(y[i+1]) 
        else:
            y.append(y[i]*2 + z[i]), z.append(y[i] + z[i]), x.append(x[i]*2), j.append(j[i]*2)

recorrer(movimientos)
print(x,y,z,j)
print("La cantidad de combinaciones posibles de " + str(movimientos) + " es de " + str(x[-1]*4+y[-1]*2+z[-1]*2+j[-1]))