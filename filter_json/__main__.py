import json
import timeit

with open("output.json", "r") as f:
    data = json.load(f)

def inputs():

    print("Escoja parámetro por el que desee filtrar.\n1- Nombre\n2- País")

    choice = input("Ingrese 1 ó 2 para continuar:")

    if choice == "1":
        name = input("Ingrese el nombre que desee filtrar: ")
        if name.capitalize() in ["Fran","Harmy","Gun","Enzo","Rodri"]:
            value = "Name"
            return filter(name,value)
        else:
            print("El nombre ingresado no se encuentra en la base de datos, vuelva a intentarlo.")

    elif choice == "2":
        name = input("Ingrese el país que desee filtrar: ")
        if name.capitalize() in get_countries(data):
            value = "Country"
            return filter(name,value)
        else:
            print("El país ingresado no se encuentra en la base de datos, vuelva a intentarlo.")

    else:
        print("Parámetro incorrecto, inténtelo de nuevo.")

def filter(name, value):

    new_output_name = [x for x in data if x[value] == name.capitalize()]

    with open("new_output_%s.json" % name, "w") as file:
        json.dump(new_output_name, file,indent=2)

def get_unique_items(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def get_countries(data):
    lista_paises=[]

    for x in data:
        lista_paises.append(x["Country"])

    return get_unique_items(lista_paises)

def main():
    start = timeit.default_timer()

    inputs()

    print("Al programa le llevo %s segundos terminar" %round(timeit.default_timer()-start,2))
if __name__ == "__main__":
    main()


