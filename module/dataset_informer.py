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


