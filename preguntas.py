"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()     
    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]
    sum = 0
    for row in data:
        sum += int(row[1])
    return sum

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]
    data =[row[0] for row in data]
    suma = {row[0]: 0 for row in data}


    for i in data:
        suma[i] = suma[i] + 1
    sum = list(suma.items())
    sum.sort(key=lambda x: x[0])
    return sum

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]
    suma = {row[0]: 0 for row in data}
    for i in data:
        suma[i[0]] = suma[i[0]] + int(i[1])
    suma = [(i, j) for i, j in suma.items()]
    suma.sort(key=lambda x: x[0])
    return suma


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]
    data = [row[2] for row in data]
    data = [i.split('-') for i in data]
    data = [mes[1] for mes in data]
    suma = {mes: 0 for mes in data}
    sum = 0
    for i in data:
        suma[i] = suma[i] + 1
    suma = [(key, value) for key, value in suma.items()]
    suma.sort(key=lambda x: x[0])
    return suma


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]
    data = [(row[0], row[1]) for row in data]
    dic = { key[0]: [0 ,10 ] for key in data}
    for i in data:
        if dic[i[0]][0] < int(i[1]):
            dic[i[0]][0] = int(i[1])

        if dic[i[0]][1] > int(i[1]):
            dic[i[0]][1] = int(i[1])
        
    list_tupla = [(key, value[0], value[1]) for key, value in dic.items()]
    list_tupla.sort(key=lambda x: x[0])
    return list_tupla


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.replace('\n', '') for row in data] 
    data = [row.split('\t') for row in data ]
    data = [row[4] for row in data]
    data = [row.split(',') for row in data]
    data = [a.split(':') for row in data for a in row]

    dic = {row[0]: [int(row[1]),  0] for row in data } 
    for i in data:
        if dic[i[0]][0] > int(i[1]):
            dic[i[0]][0] = int(i[1])

        if dic[i[0]][1] < int(i[1]):
            dic[i[0]][1] = int(i[1])

    list_tuple = [(key, value[0], value[1]) for key, value in dic.items()]

    list_tuple.sort(key=lambda x: x[0])
    return list_tuple
    



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t')[:2] for row in data ]
    data = [[row[0], int(row[1])] for row in data]
    dic = {key[1] : [] for key in data}
    for i in data:
        # if i[0] not in dic[i[1]]:
        dic[i[1]].append(i[0])

    list_data = [(key, value) for key, value in dic.items()]
    list_data.sort(key=lambda x: x[0])
    return list_data

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t')[:2] for row in data ]
    data = [[row[0], int(row[1])] for row in data]
    dic = {key[1] : [] for key in data}
    for i in data:
        if i[0] not in dic[i[1]]:
            dic[i[1]].append(i[0])

    list_data = [(key, sorted(value)) for key, value in dic.items()]
    list_data.sort(key=lambda x: x[0])
    return list_data


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t')[4] for row in data]
    data = [row.split(',') for row in data]
    data = [key.split(':')[0] for row in data for key in row]
    dic = {key:0 for key in data}
    for i in data:
        dic[i]+=1
    return dic


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]
    data = [[row[0], row[3].split(','), row[4].split(',')] for row in data]
    lis_tuple = [(row[0], len(row[1]), len(row[2])) for row in data]
    return lis_tuple


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]
    data = [[row[1], row[3].split(',')] for row in data]

    data = [[int(row[0]), i] for row in data for i in row[1]] 
    dic = {letra[1]:0 for letra in data}
    for i in data:
        dic[i[1]] += i[0]
    list_tupla = [(key, value) for key, value in dic.items()]
    list_tupla.sort(key =lambda x: x[0])
    return dict(list_tupla)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import re
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.replace('\n','') for row in data]
    data = [row.split('\t') for row in data]
    data = [[col[0], col[4]] for col in data]
    # data = [[row[0], re.findall(r'(?<=:)\w+', row[1])] for row in data]
    data = [[row[0], re.findall(r'\d+', row[1])] for row in data]
    data = [[row[0], sum([int(a) for a in row[1]])] for row in data ]

    dic = { letra[0] : 0 for letra in data}

    for i in data:
        dic[i[0]] += i[1]
    list_out = [(i, j) for i,j in dic.items()]
    list_out.sort(key = lambda x: x[0])
    return list_out
