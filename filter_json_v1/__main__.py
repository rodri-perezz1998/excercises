import json
import timeit

VAR_NAME_ES = 'nombre'
VAR_COUNTRY_ES = 'pais'
VAR_NAME = 'Name'
VAR_COUNTRY = 'Country'


def filters(name, value, data, list_to_compare, ):
    if name.capitalize() in list_to_compare:
        start = timeit.default_timer()

        with open("new_output_%s.json" % name, "w") as file:
            json.dump([x for x in data if x[value] == name.capitalize()], file, indent=2)

        print("\n >>> Al programa le llevó %s segundos terminar. <<< " % (timeit.default_timer() - start))
    else:
        print("\nNo se encontró el {} en la base de datos, intentelo de nuevo.".format(name))


def get_unique_items(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def get_countries(data):
    lists = []

    for x in data:
        lists.append(x['Country'])

    return get_unique_items(lists)


def app():
    with open("output.json", "r") as file:
        data = json.load(file)

    print('Seleccione mediante qué parámetro desea filtrar :\n- Nombre\n- País')

    choice = input("\nEscoja un parámetro para continuar: ")

    if choice.lower() == VAR_NAME_ES:
        filters(input("\nIngrese el nombre que desee filtrar: "),
                VAR_NAME,
                data,
                ["Fran", "Harmy", "Enzo", "Gun", "Rodri"]
                )

    elif choice.lower() == VAR_COUNTRY_ES:
        filters(input("\nIngrese el país que desee filtrar:"),
                VAR_COUNTRY,
                data,
                get_countries(data)
                )

    else:
        print("\nParametro erróneo, vuelva a intentarlo por favor.")


if __name__ == '__main__':
    app()
