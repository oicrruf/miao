import app
import crud

def main():
    print(chr(27) + "[2J")
    crud.read()

    print("[0] Salir")
    print("[1] Ingresar un nuevo registro")
    print("\n")

    option = input("Option: ")
    # if (option == "1"):

    if (option == "1"):
        crud.create()

# if __name__ == "__main__":
#     main()