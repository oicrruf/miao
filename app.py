from atexit import register
from fileinput import close
import json
import uuid
import pandas as pd
from tabulate import tabulate
import uuid
from datetime import datetime


def run():
    print(chr(27) + "[2J")
    read_file()

    print("[0] Salir")
    print("[1] Ingresar un nuevo registro")
    print("\n")

    option = input()
    # if (option == "1"):

    if (option == "1"):
        set_register()

    if (option == "0"):
        close()


def read_file():

    # encoding="utf-8", para leer correctamente el archivo
    with open("data.json", "r", encoding="utf-8") as json_file:
        registers = json.load(json_file)
        columns = registers["columns"]

        df = pd.DataFrame(registers["data"], columns=columns)
        df["type"].replace(True, "in", inplace=True)
        df["type"].replace(False, "out", inplace=True)
        df["paid"].replace(True, "X", inplace=True)
        df["paid"].replace(False, "-", inplace=True)
        df["optional"].replace(True, "X", inplace=True)
        df["optional"].replace(False, "-", inplace=True)
        df["recurring"].replace(True, "X", inplace=True)
        df["recurring"].replace(False, "-", inplace=True)
        df["available"].replace(True, "X", inplace=True)
        df["available"].replace(False, "-", inplace=True)
        df["amount"] = "$" + df["amount"].astype(str)

        print("\n")
        print(tabulate(df, showindex=False, headers=df.columns))
        print("\n")


def set_register():

    with open("data.json", "r", encoding="utf-8") as json_file:
        id = str(uuid.uuid1())
        register = {}
        registers = json.load(json_file)
        columns = registers["columns"]

        for column in columns:
            register["id"] = id
            if column != "id":
                value = input(column.capitalize() + ": ")
                if value.lower() == 'y' and value != "":
                    register[column] = True
                elif value.lower() == 'n' and value != "":
                    register[column] = False
                elif value != "":
                    if column == "date":
                        register[column] = str(
                            datetime.strptime(value, '%d/%m/%y'))
                    if column == "amount":
                        register[column] = float(value)
                    else:
                        register[column] = value.lstrip()

        data = registers["data"]
        data.append(register)

        with open('data.json', 'w') as json_file:
            add_register = {"columns": columns, "data": data}
            json.dump(add_register, json_file, sort_keys=False, indent=4)

    print("\n")
    read_file()


if __name__ == "__main__":
    run()
