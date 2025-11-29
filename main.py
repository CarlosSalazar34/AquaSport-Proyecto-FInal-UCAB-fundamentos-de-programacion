import os

def sales_of_the_month(content_two: str) -> None:
    total_sales_first_month: int = 0
    total_sales_second_month: int = 0
    total_sales_third_month: int = 0

    total_first_month: int = 0
    total_second_month: int = 0
    total_third_month: int = 0
    
    for i in range(1, len(content_two)):
        month: int = int(content_two[i].split(",")[0].split("/")[1])
        match month:
            case 10:
                total_day: int = sum_of_the_day(content_two[i].split(",")[1::])
                total_sales_first_month += len(content_two[i].split(",")[1::])
                total_first_month += total_day
            case 11:
                total_day: int = sum_of_the_day(content_two[i].split(",")[1::])
                total_sales_second_month += len(content_two[i].split(",")[1::])
                total_second_month += total_day
            case 12:
                total_day: int = sum_of_the_day(content_two[i].split(",")[1::])
                total_sales_third_month += len(content_two[i].split(",")[1::])
                total_third_month += total_day

    print(f"El total de ganacias del mes de Octubre es: {total_first_month} $")
    print(f"El total de ventas del mes de Octubre es: {total_sales_first_month} ventas")
    print("-------------------------------")
    print(f"El total de ganancias del mes de Noviembre es: {total_second_month} $")
    print(f"El total de ventas del mes de Noviembre es: {total_sales_second_month} ventas")
    print("-------------------------------")
    print(f"El total de ganancias del mes de Diciembre es: {total_third_month} $")
    print(f"El total de ventas del mes de Diciembre es: {total_sales_third_month} ventas")


def get_price_of_product(content_one: list[str],code: str) -> int:
    for line  in content_one:
        data = line.split(",")
        if data[1] == code:
            return float(data[-1])
        
def get_total_of_the_day(content_two: str) -> None:
    for d in content_two[1::]:
        day = d[1::].split(",")[0]
        data = d[1::].split(",")[1::]
        total: int = sum_of_the_day(data)
        
        print(f"El total de ventas del dia {day} es {len(data)} y se obtuvo una ganacia de: {total}$")

def sum_of_the_day(sales: list[str]) -> int:
    total: int = 0
    for item in sales:
        total += int(item)
    return total

def get_total(list: list) -> int:
    total: int = 0
    for item in list:
        total += item
    return total


def total_of_sales(content_two: str, content_one: str) -> list[int]:
    total_ventas: int = 0
    total_usd: int = 0

    for line in content_two[1::]:
        data = line[1:-1].split(",")
        for price in data[1::]:
            total_ventas += int(price)


    columns: list[int] = []

    for item in content_two[0].split(",")[1::]:
        columns.append(item.replace("\n", ""))

        codes: list[list[str, list[str]]] = []
        
        for code in columns:
            codes.append([code, []])

        for i in range(0, len(columns)):
            for j in range(1, len(content_two)):
                data = content_two[j].split(",")[1::]
                for v in range(0, len(data)):
                    if v == i:
                        for item in codes:
                            # print(item)
                            if item[0] == columns[i]:
                                item[1].append(int(data[v].replace("\n", "")))

        for item in codes:
            price: int = get_price_of_product(content_one=content_one, code=item[0])
            ventas: int = get_total(item[1])
            total_usd += ventas * price
    return [total_ventas, total_usd]

def get_total_of_all_products(content_two: str, content_one: str) -> None:
    columns: list[int] = []

    for item in content_two[0].split(",")[1::]:
        columns.append(item.replace("\n", ""))

    codes: list[list[str, list[str]]] = []
    
    for code in columns:
        codes.append([code, []])

    for i in range(0, len(columns)):
        # print(f"indice {i}")
        # print(content_two)
        for j in range(1, len(content_two)):
            data = content_two[j].split(",")[1::]
            for v in range(0, len(data)):
                if v == i:
                    for item in codes:
                        # print(item)
                        if item[0] == columns[i]:
                            item[1].append(int(data[v].replace("\n", "")))

    for item in codes:
        price: int = get_price_of_product(content_one=content_one, code=item[0])
        ventas: int = get_total(item[1])
        print("El total de ventas del codigo "+item[0], end=" => ")
        print(str(ventas)+" ventas")
        print(f"El total de ingresos del producto es {ventas*price:.2f}$")
        print("-------------------------------")


def read_file(file_path_price: str, file_path_sales: str) -> str:
    with open(file_path_price, "r", encoding="utf-8") as file_price:
        content_one = file_price.readlines()

    
    with open(file_path_sales, "r", encoding="utf-8") as file_sales:
        content_two = file_sales.readlines()

    ventas, total_usd = total_of_sales(content_two=content_two, content_one=content_one)
    print(f"El total de ventas del trimestre es: {ventas} ventas")
    print(f"El total de ingresos del trimestre es: {total_usd:.2f}$")
    print("-------------------------------")
    print("El total de ventas por producto es el siguiente: ")
    get_total_of_all_products(content_two=content_two, content_one=content_one)  

    """En proceso"""
    get_total_of_the_day(content_two=content_two)
    sales_of_the_month(content_two=content_two)

    

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
        choice: str = input("Ingrese su opción: ").lower().strip()

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