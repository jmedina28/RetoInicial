
recorrido = []
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

def movimientos(casilla):
    
        for i in range(len(diccionario[casilla])):
            posicion = i
            recorrido.append(diccionario[casilla][posicion])
        return recorrido



def recorrido_total(casilla):
    recorrido_total = []
    recorrido_total.append(movimientos(casilla))
    for i in range(len(recorrido_total[i])):
        for j in range(len(recorrido_total[i])):
            recorrido_total.append(movimientos(recorrido))
    return recorrido_total
print(recorrido_total(1))
    
   
    


    

