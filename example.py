import os

def histogram(content_one: str, content_two: str) -> str:
    content: str = ""
    total = total_of_sales(content_two=content_two, content_one=content_one)[0]
    print("hola")
    histogram_values: list[list[str, int]] = []
    content += "Representación gráfica de las ventas por producto:\n"
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
        ventas: int = get_total(item[1])
        histogram_values.append([item[0], ventas])

    content += f'{"*"*50}\n'
    # content += "Representación gráfica de las ventas por producto:\n"
    for item in histogram_values:
        content += "#"*int((item[1]*100)/total) + f" {get_name_of_product(content_one, item[0])} ({(item[1]*100)/total:.2f}%)\n"
    content += f'{"*"*50}\n'
    return content

def get_max(sales: list[int]) -> int:
    max_value: int = sales[0]
    for item in sales:
        if item > max_value:
            max_value = item
    return max_value

def get_name_of_product(content_one: str, code: str) -> str:
    for line in content_one:
        data = line.split(",")
        if data[1] == code:
            return data[0]
    return ""


def get_product_less_sold(content_two: str, content_one: str) -> str:
    content: str = ""
    columns: list[str] = content_two[0].split(",")[1::]
    sales = []
    prices = []
    for product in content_one:
        data = product.split(",")
        prices.append(float(data[-1]))

    codes: list[list[str, list[int]]] = []
    for code in columns:
        codes.append([code, []])

    for i in range(1, len(content_two)):
        data = content_two[i].split(",")[1::]
        for v in range(0, len(data)):
            for item in codes:
                if item[0] == columns[v]:
                    item[1].append(int(data[v].replace("\n", "")))
                    item.append(prices[v])

    content += "Producto menos vendido en el trimestre fue el: "
    for item in codes:
        sales.append(get_total(item[1]))

    min_sales = get_max(sales)
    for item in codes:
        if get_total(item[1]) < min_sales:
            min_sales = get_total(item[1])

    for item in codes:
        if get_total(item[1]) == min_sales:
            price = item[2]
            content += get_name_of_product(content_one=content_one, code=item[0]) + "\n"
            content += f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el trimestre" + " => "
            content += str(min_sales)+" ventas\n"  
            content += f"El total de ingresos que dejo este producto fue {min_sales * price:.2f}$\n"
            break
    return content

def get_product_most_sold(content_two: str, content_one: str) -> str:
    content: str = ""
    columns: list[str] = content_two[0].split(",")[1::]
    sales = []
    prices = []
    for product in content_one:
        data = product.split(",")
        prices.append(float(data[-1]))

    codes: list[list[str, list[int]]] = []
    for code in columns:
        codes.append([code, []])

    for i in range(1, len(content_two)):
        data = content_two[i].split(",")[1::]
        for v in range(0, len(data)):
            for item in codes:
                if item[0] == columns[v]:
                    item[1].append(int(data[v].replace("\n", "")))
                    item.append(prices[v])

    content += "Producto más vendido en el trimestre fue el: "
    for item in codes:
        sales.append(get_total(item[1]))

    max_sales = get_max(sales)
    for item in codes:
        if get_total(item[1]) == max_sales:
            price = item[2]
            content += get_name_of_product(content_one=content_one, code=item[0]) + "\n"
            content += f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el trimestre" + " => "
            content += str(max_sales)+" ventas\n"
            content += f"El total de ingresos que dejo este producto fue {max_sales * price:.2f}$\n"
            break
    return content

def sales_of_the_month_for_product(content_two: str, content_one: str) -> str:
    content: str = ""
    columns: list[str] = content_two[0].split(",")[1::]

    prices = []

    for product in content_one:
        data = product.split(",")
        prices.append(float(data[-1]))

    month_one: list[list[str, list[int]]] = []
    month_two: list[list[str, list[int]]] = []
    month_three: list[list[str, list[int]]] = []

    for c in columns:
        month_one.append([c, []])
        month_two.append([c, []])
        month_three.append([c, []])

    for i in range(1, len(content_two)):
        if content_two[i].split(",")[0].split("/")[1] == "10":
            data = content_two[i].split(",")[1::]
            for v in range(0, len(data)):
                for item in month_one:
                    if item[0] == columns[v]:
                        item[1].append(int(data[v].replace("\n", "")))
                        item.append(prices[v])

        if content_two[i].split(",")[0].split("/")[1] == "11":
            data = content_two[i].split(",")[1::]
            for v in range(0, len(data)):
                for item in month_two:
                    if item[0] == columns[v]:
                        item[1].append(int(data[v].replace("\n", "")))
                        item.append(prices[v])
        
        if content_two[i].split(",")[0].split("/")[1] == "12":
            data = content_two[i].split(",")[1::]
            for v in range(0, len(data)):
                for item in month_three:
                    if item[0] == columns[v]:
                        item[1].append(int(data[v].replace("\n", "")))
                        item.append(prices[v])

    # print(month_one)

    content += "Ventas del mes de Octubre por producto:\n"
    for item in month_one:
        price = item[2]
        total: int = get_total(item[1])
        content += f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el mes de octubre" + " => "
        content += str(total)+" ventas\n"
        content += f"El total de ingresos que dejo este producto fue {total * price:.2f}$\n"

    content += "-------------------------------\n"
    content += "Ventas del mes de Noviembre por producto:\n"
    for item in month_two:
        price = item[2]
        total: int = get_total(item[1])
        content += f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el mes de noviembre" + " => "
        content += str(total)+" ventas\n"
        content += f"El total de ingresos que dejo este producto fue {total * price:.2f}$\n"
    
    content += "-------------------------------\n"
    content += "Ventas del mes de Diciembre por producto:\n"
    for item in month_three:
        price = item[2]
        total: int = get_total(item[1])
        content += f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el mes de diciembre" + " => "
        content += str(total)+" ventas\n"
        content += f"El total de ingresos que dejo este producto fue {total * price:.2f}$\n"
    
    return content


def sales_of_the_month(content_two: str, content_one: str) -> str:
    content: str = ""
    prices = []
    for product in content_one:
        data = product.split(",")
        prices.append(float(data[-1]))

    columns: list[str] = content_two[0].split(",")[1::] 

    codes: list[list[str, list[int]]] = []

    for code in columns:
        codes.append([code, []])


    total_sales_first_month: int = 0
    total_sales_second_month: int = 0
    total_sales_third_month: int = 0

    total_first_month: int = 0
    total_second_month: int = 0
    total_third_month: int = 0

    for line in range(1, len(content_two)):
        if content_two[line].split(",")[0].split("/")[1] == "10":
            data = content_two[line].split(",")[1::]
            for v in range(0, len(data)):
                total_sales_first_month += int(data[v]) * prices[v]
            total_first_month += get_total(data)

        if content_two[line].split(",")[0].split("/")[1] == "11":
            data = content_two[line].split(",")[1::]
            for v in range(0, len(data)):
                total_sales_second_month += int(data[v]) * prices[v]
            total_second_month += get_total(data)

        if content_two[line].split(",")[0].split("/")[1] == "12":
            data = content_two[line].split(",")[1::]
            for v in range(0, len(data)):
                total_sales_third_month += int(data[v]) * prices[v]
            total_third_month += get_total(data)

    content += f"El total de ventas del mes de Octubre es: {total_first_month} ventas\n"
    content += f"El total de ingresos del mes de Octubre es: {total_sales_first_month:.2f}$\n"
    content += "-------------------------------\n"
    content += f"El total de ventas del mes de Noviembre es: {total_second_month} ventas\n"
    content += f"El total de ingresos del mes de Noviembre es: {total_sales_second_month:.2f}$\n"
    content += "-------------------------------\n"
    content += f"El total de ventas del mes de Diciembre es: {total_third_month} ventas\n"
    content += f"El total de ingresos del mes de Diciembre es: {total_sales_third_month:.2f}$\n"
    content += "-------------------------------\n"

    return content


def get_price_of_product(content_one: list[str],code: str) -> int:
    for line  in content_one:
        data = line.split(",")
        if data[1] == code:
            return float(data[-1])
        
def get_total_of_the_day(content_two: str) -> str:
    content: str = ""
    for d in content_two[1::]:
        day = d[1::].split(",")[0]
        data = d[1::].split(",")[1::]
        total: int = sum_of_the_day(data)
        
        content += f"El total de ventas del dia {day} es {len(data)} y se obtuvo una ganacia de: {total}$\n"
    return content

def sum_of_the_day(sales: list[str]) -> int:
    total: int = 0
    for item in sales:
        total += int(item)
    return total

def get_total(list: list) -> int:
    total: int = 0
    for item in list:
        total += int(item)
    return total


def total_of_sales(content_two: str, content_one: str) -> list[int]:
    total_ventas = 0
    total_usd = 0

    columns = []
    for item in content_two[0].split(",")[1::]:
        columns.append(item.replace("\n", ""))

    codes: list[list] = []
    for code in columns:
        codes.append([code, []])

    precios = []
    for line in content_one:
        data = line.strip().split(",")
        precios.append(float(data[-1]))

    for row in content_two[1::]:
        data = row.strip().split(",")[1::]

        for i in range(len(columns)):
            units = int(data[i])
            codes[i][1].append(units)
            total_ventas += units  

    for i in range(len(codes)):
        ventas_totales = get_total(codes[i][1])
        total_usd += ventas_totales * precios[i]

    return [total_ventas, total_usd]

def get_total_of_all_products(content_two: str, content_one: str) -> str:
    # content: str = ""
    columns: list[int] = []
    # print(content_two)

    for item in content_two[0].split(",")[1::]:
        # ACCEDO AL VALOR DE LA LISTA 
        # 'fecha,AB-01,RX-12,HO-25,HQ-22,GR-12,PR-14,AF-56,ST-10,AT-24,HF-02\n'
        columns.append(item.replace("\n", ""))

    codes: list[list[str, list[str]]] = []
    
    for code in columns:
        codes.append([code, []])
    
    # print(codes)

    for i in range(0, len(columns)):
        # print(columns[i])
        for j in range(1, len(content_two)):
            data = content_two[j].split(",")[1::]
            # print(data)
            for v in range(0, len(data)):
                if v == i:
                    for item in codes:
                        if item[0] == columns[i]:
                            item[1].append(int(data[v].replace("\n", "")))

    # print(codes)
    # print(len(codes[1][1]))
    # print(len(content_two[1::]))

    for item in codes:
        price: int = get_price_of_product(content_one=content_one, code=item[0])
        ventas: int = get_total(item[1])
    
        # print(f"El total de ventas del codigo {item[0]} es {ventas} ventas\n")
        # print(f"El total de ingresos del producto es {ventas*price:.2f}$\n")
    #     content += f"El total de ventas del codigo {item[0]} es {ventas} ventas\n"
    #     content += f"El total de ingresos del producto es {ventas*price:.2f}$\n"
    #     content += "-------------------------------\n"

    # return content


def read_file(file_path_price: str, file_path_sales: str) -> str:
    with open(file_path_price, "r", encoding="utf-8") as file_price:
        content_one = file_price.readlines()

    
    with open(file_path_sales, "r", encoding="utf-8") as file_sales:
        content_two = file_sales.readlines()

    # get_total_of_all_products(content_two=content_two, content_one=content_one)
    histograma = histogram(content_one=content_one, content_two=content_two)
    print(histograma)

def menu():
    print()
    print("BIENVENIDO AL SISTEMA DE REPORTES DE VENTAS".center(50, "-"))
    print("TRIMESTRALES DE PRODUCTOS".center(50, "-"))
    print()
    print("Presione 1 para leer el reporte de ventas del trimestre: ")
    print("Presione 0 para salir.")
    print()

def main()->None:
    while True:
        os.system("cls")            
        menu()
        choice: str = input("Ingrese su opción: ").lower().strip()

        match choice: 
            case "1":
                os.system("cls")
                print("ARCHIVOS DISPONIBLES".center(50, "*"))
                for i in os.listdir():
                    if "txt" in i:
                        print(i)
                    else:
                        continue
                # file_price: str = input("Ingrese la ruta del archivo de precios: ")
                # file_sales: str = input("Ingrese la ruta del archivo de ventas: ")
                file_price: str = "precios_natacion.txt"
                file_sales: str = "ventas_natacion.txt"
                read_file(file_path_price=file_price, file_path_sales=file_sales)
                print("Reporte generado exitosamente en reporte_de_ventas.txt")
                input("Presione Enter para continuar...")
            
            case "0":
                break

            case _:
                os.system("cls")
                print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para continuar...")
                

if __name__ == "__main__":
    main()