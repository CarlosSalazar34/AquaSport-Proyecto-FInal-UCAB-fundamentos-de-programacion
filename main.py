import os

def get_total(list: list) -> int:
    total: int = 0
    for item in list:
        total += item
    return total


def total_of_sales(content: str) -> int:
    total: int = 0

    for line in content[1::]:
        data = line[1:-1].split(",")
        for price in data[1::]:
            total += int(price)
    return total

def get_total_of_all_products(content_two: str) -> None:
    columns: list[int] = []

    for item in content_two[0].split(",")[1::]:
        columns.append(item.replace("\n", ""))

    codes: list[list[str, list[str]]] = []
    
    for code in columns:
        codes.append([code, []])

    for i in range(0, len(columns)):
        print(f"indice {i}")
        for j in range(1, len(content_two)):
            data = content_two[j].split(",")[1::]
            for v in range(0, len(data)):
                if v == i:
                    for item in codes:
                        # print(item)
                        if item[0] == columns[i]:
                            item[1].append(int(data[v].replace("\n", "")))

    for item in codes:
        print(get_total(item[1]))
    # return codes


    

def read_file(file_path_price: str, file_path_sales: str) -> str:
    # os.system("cls")
    with open(file_path_price, "r", encoding="utf-8") as file_price:
        content_one = file_price.readlines()

    
    with open(file_path_sales, "r", encoding="utf-8") as file_sales:
        content_two = file_sales.readlines()


    total: int = total_of_sales(content=content_two)
    # total_of_all_products: list[list[int]] = get_total_of_all_products(content_two=content_two)

    # for item in total_of_all_products:
        # print(get_total(item[1]))

    print(f"El total de ventas del trimestre es: {total}")
    get_total_of_all_products(content_two=content_two)  
    # print(total_of_all_products)

    
    # return content_two[0:2]

def menu():
    print()
    print("BIENVENIDO AL SISTEMA DE REPORTES DE VENTAS".center(50, "-"))
    print("TRIMESTRALES DE PRODUCTOS".center(50, "-"))
    print()
    print("Presione 1 para leer el reporte de ventas del trimestre: ")
    print("Presione 0 para salir.")
    print()

def main():
    while True:
        os.system("cls")            
        menu()
        choice: str = input("Ingrese su opción: ")

        match choice: 
            case "1":
                os.system("cls")
                file_price: str = input("Ingrese la ruta del archivo de precios: ")
                file_sales: str = input("Ingrese la ruta del archivo de ventas: ")
                print("")
                print(read_file(file_path_price=file_price, file_path_sales=file_sales))
                input("Presione Enter para continuar...")
            
            case "0":
                break

            case _:
                os.system("cls")
                print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para continuar...")
                

if __name__ == "__main__":
    main()