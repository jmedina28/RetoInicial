
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

casilla = 0

def recorrer1(nmov):
    posibilidad1 = []
    for p in range(nmov):
        for i in range(len(diccionario[casilla])):
            posicion = i
            posibilidad1.append(diccionario[casilla][posicion])
        print(posibilidad1)
        print(len(posibilidad1))
        for n in range(len(posibilidad1)):
            posibilidad1.extend(diccionario[posibilidad1[n]])
     
    print(posibilidad1)
    
    
recorrer1(1)


    
   
    


    

