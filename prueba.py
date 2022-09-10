

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

    print("------------------------------------------------------------------")
# si sumas todos los valores que se encuentran antes de la linea divisoria obtienes el resultado de 5 movimientos.
