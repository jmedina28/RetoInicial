
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


    
   
    


    

