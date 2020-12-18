import csv


def read_csv():
    with open("cotizacion.csv", "r") as csv_file:
        lines = csv_file.readlines()

    values = [i[:-1].split(",") for i in lines[1:len(lines)]]
    dict_list = []

    for i in values:
        x = {"Nombre": i[0], "Final": i[1], "Maximo": i[2], "Minimo": i[3], "Volumen": i[4], "Efectivo": i[5]}
        dict_list.append(x)

    ops(dict_list)


def ops(dict_list):
    final = [float(x["Final"]) for x in dict_list]
    maximo = [float(x["Maximo"]) for x in dict_list]
    minimo = [float(x["Minimo"]) for x in dict_list]
    volumen = [float(x["Volumen"]) for x in dict_list]
    efectivo = [float(x["Efectivo"]) for x in dict_list]

    mins = (str(min(final)), str(min(maximo)), str(min(minimo)), str(min(volumen)), str(min(efectivo)))
    maxs = (str(max(final)), str(max(maximo)), str(max(minimo)), str(max(volumen)), str(max(efectivo)))
    meds = (str(round(sum(final) / len(final), 1)), str(round(sum(maximo) / len(maximo), 1)),
            str(round(sum(minimo) / len(minimo), 1)), str(round(sum(volumen) / len(volumen), 1)),
            str(round(sum(efectivo) / len(efectivo), 1)))

    for x in dict_list:
        del (x["Nombre"])

    write(mins, maxs, meds)


def write(mins, maxs, meds):
    keys = ["Final", "Maximo", "Minimo", "Volumen", "Efectivo"]

    with open("resultado.csv", "w") as f:

        f.write("Tipo")
        for x in keys:
            f.write(";" + x)
        f.write("\nMinimo")
        for x in mins:
            f.write(";" + str(x))
        f.write("\nMaximo")
        for x in maxs:
            f.write(";" + str(x))
        f.write("\nMedia")
        for x in meds:
            f.write(";" + str(x))


if __name__ == "__main__":
    read_csv()
