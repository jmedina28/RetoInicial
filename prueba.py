
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

for u in range(len(diccionario)):
    def recorrer1():
        global posibilidad1
        posibilidad1 = []
        for i in range(len(diccionario[u])):
            posicion = i
            posibilidad1.append(diccionario[u][posicion])
        return posibilidad1

    print(recorrer1()), print(len(posibilidad1))

    def recorrer2():
        global posibilidad2
        posibilidad2 = []
        for i in range(len(posibilidad1)):
            posicion = i
            posibilidad2.extend(diccionario[posibilidad1[posicion]])
        return posibilidad2
    print(recorrer2()), print(len(posibilidad2))
    
    def recorrer3():
        global posibilidad3
        posibilidad3 = []
        for i in range(len(posibilidad2)):
            posicion = i
            posibilidad3.extend(diccionario[posibilidad2[posicion]])
        return posibilidad3
    print(recorrer3()), print(len(posibilidad3))

    def recorrer4():
        global posibilidad4
        posibilidad4 = []
        for i in range(len(posibilidad3)):
            posicion = i
            posibilidad4.extend(diccionario[posibilidad3[posicion]])
        return posibilidad4
    print(recorrer4()), print(len(posibilidad4))

    def recorrer5():
        global posibilidad5
        posibilidad5 = []
        for i in range(len(posibilidad4)):
            posicion = i
            posibilidad5.extend(diccionario[posibilidad4[posicion]])
        return posibilidad5
    print(recorrer5()), print(len(posibilidad5))

    def recorrer6():
        global posibilidad6
        posibilidad6 = []
        for i in range(len(posibilidad5)):
            posicion = i
            posibilidad6.extend(diccionario[posibilidad5[posicion]])
        return posibilidad6
    print(recorrer6()), print(len(posibilidad6))

    def recorrer7():
        global posibilidad7
        posibilidad7 = []
        for i in range(len(posibilidad6)):
            posicion = i
            posibilidad7.extend(diccionario[posibilidad6[posicion]])
        return posibilidad7
    print(recorrer7()), print(len(posibilidad7))

    def recorrer8():
        global posibilidad8
        posibilidad8 = []
        for i in range(len(posibilidad7)):
            posicion = i
            posibilidad8.extend(diccionario[posibilidad7[posicion]])
        return posibilidad8
    print(recorrer8()), print(len(posibilidad8))
    

    posibilidad.extend(posibilidad8)

    
    print("------------------------------------------------------------------")
print("La cantidad de posibles combinaciones de 8   movimientos que se pueden realizar es: ", len(posibilidad))

