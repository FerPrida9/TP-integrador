import csv

def without_repeated(route, index):
    '''This function returns a list without repeteated elements'''
    with open(route, encoding= 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        type_list = []

        for line in reader:
            type_list.append(line[index])

    new_list = set(type_list)
    return new_list

def menu():
    '''This function is a menu to choose the elevation 
    of the airport. Returns the value entered'''

    print("""Ingrese el tipo de elevacion de aeropuerto que quiere visualizar
         1._ Bajo
         2._ Medio
         3._ Alto
         """)
    
    while True:
        elevation = (input())
        if elevation == "1" or elevation == "2" or elevation == "3":
            break
        else:
            print("Ingresaste un valor incorrecto, ingresa un valor entre 1-3")
            continue
    return elevation

def airports_by_elevation(route):
    '''This function returns '''
    elevation = menu()

    with open(route, encoding= 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        type_list = []

        for line in reader:
            if elevation == "1":
                if(line[23] == "bajo"):
                    type_list.append(line[3])
            elif elevation == "2":
                if(line[23] == "medio"):
                    type_list.append(line[3])
            else:
                if(line[23] == "alto"):
                    type_list.append(line[3])

    return type_list

def remove_accent(word):
    '''This function returns the word without accent'''
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
               'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    word_without_accent = ''.join([accents.get(letter, letter) for letter in word])
    return word_without_accent

def airports_in_capitals (route1, route2):
    '''This function returns a dict with the airports in the capital of each province'''
    capital = 6
    city = 0
    municipality = 13
    name = 3
    with open(route1, encoding = 'utf-8') as capitals_file, open (route2, encoding = 'utf-8') as airports_file:
        reader = csv.reader(capitals_file)
        next (reader)
        capitals_list = []
        for line in reader:
                if line[capital] == 'admin':
                        city_without_accent = remove_accent(line[city])
                        capitals_list.append(city_without_accent)
        reader = csv.reader (airports_file)
        next(reader)
        airports_dict = {}
        for line in reader:
                city_without_accent = remove_accent(line[municipality])
                if city_without_accent in capitals_list:
                        if city_without_accent not in airports_dict:
                                airports_dict[city_without_accent] = []
                        airports_dict[city_without_accent].append(line[name])
    return airports_dict

def menu2():
    ''' This function is a menu to choose the surface of the lakes'''
    print ('''Ingrese la superficie de lagos que desea visualizar (ingresar palabra en minuscula):
            1) Chico
            2) Medio
            3) Grande
            ''')
    while True:
        surface = (input())
        if surface == 'chico' or surface == 'medio' or surface == 'grande':
            break
        else:
            print ('Ingresaste mal la superficie, ingrese una de las 3 sugeridas')
            continue
    return surface

def lakes_by_surface(route):
    '''This function returns a list with the lakes of one category (little, medium or big)'''
    size = 9
    name = 0
    surface = menu2()
    with open (route, encoding = 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        lakes_list = []
        for line in reader:
            if line[size] == surface:
                lakes_list.append(line[name])
    return lakes_list

def street_situation (route):
    '''This function returns a list of tuples with the five jurisdictions with the largest homeless pupulation'''
    jurisdiction = 0
    percent = 13
    with open (route, encoding = 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)
        jurisdiction_dict = {}
        for line in reader:
            jurisdiction_dict[line[jurisdiction]] = line[percent]
        list_ordered = sorted (jurisdiction_dict.items(), key = lambda x: x[1], reverse = True)
        max_5 = list_ordered[:5]
    return max_5