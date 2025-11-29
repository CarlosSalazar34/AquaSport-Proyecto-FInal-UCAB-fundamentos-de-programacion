import os

def histogram(content_one: str, content_two: str) -> str:
    content: str = ""
    total = total_of_sales(content_two=content_two, content_one=content_one)[0]
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

    # for item in histogram_values:
    #     percentage: float = (item[1] / total) * 100
    #     stars: int = int(percentage // 2)
    #     print(f"Codigo {item[0]}: " + "*" * stars + f" ({percentage:.2f}%)")


    # print("*" * 50, end="\n")
    content += f'{"*"*50}\n'
    # print("Representación gráfica de las ventas por producto:")
    content += "Representación gráfica de las ventas por producto:\n"
    for item in histogram_values:
        content += "#"*int((item[1]/total)*100) + f" {get_name_of_product(content_one, item[0])} ({(item[1]/total)*100:.2f}%)\n"
        # print("#"*int((item[1]/total)*100), f"{get_name_of_product(content_one, item[0])} ({(item[1]/total)*100:.2f}%)")
    content += f'{"*"*50}\n'
    return content
    # print(("*" * 50), end="\n")

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

    # print("Producto menos vendido en el trimestre fue el: ", end="")
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
            # print(get_name_of_product(content_one=content_one, code=item[0]))
            # print(f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el trimestre", end=" => ")
            # print(str(min_sales)+" ventas")
            # print(f"El total de ingresos que dejo este producto fue {min_sales * price:.2f}$")
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

    # print("Producto más vendido en el trimestre fue el: ", end="")
    content += "Producto más vendido en el trimestre fue el: "
    for item in codes:
        sales.append(get_total(item[1]))

    max_sales = get_max(sales)
    for item in codes:
        if get_total(item[1]) == max_sales:
            price = item[2]
            # print(get_name_of_product(content_one=content_one, code=item[0]))
            # print(f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el trimestre", end=" => ")
            # print(str(max_sales)+" ventas")
            # print(f"El total de ingresos que dejo este producto fue {max_sales * price:.2f}$")
            content += get_name_of_product(content_one=content_one, code=item[0]) + "\n"
            content += f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el trimestre" + " => "
            content += str(max_sales)+" ventas\n"
            content += f"El total de ingresos que dejo este producto fue {max_sales * price:.2f}$\n"
            break
    return content

        # price = item[2]
        # total: int = get_total(item[1])
        # print(f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el trimestre", end=" => ")
        # print(str(total)+" ventas")
        # print(f"El total de ingresos que dejo este producto fue {total * price:.2f}$")

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
        # print(content_two[i])
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

    # print("Ventas del mes de Octubre por producto:")
    content += "Ventas del mes de Octubre por producto:\n"
    for item in month_one:
        price = item[2]
        total: int = get_total(item[1])
        # print(f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el mes de octubre", end=" => ")
        # print(str(total)+" ventas")
        # print(f"El total de ingresos que dejo este producto fue {total * price:.2f}$")
        content += f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el mes de octubre" + " => "
        content += str(total)+" ventas\n"
        content += f"El total de ingresos que dejo este producto fue {total * price:.2f}$\n"

    # print("-------------------------------")
    # print("Ventas del mes de Noviembre por producto:")
    content += "-------------------------------\n"
    content += "Ventas del mes de Noviembre por producto:\n"
    for item in month_two:
        price = item[2]
        total: int = get_total(item[1])
        # print(f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el mes de noviembre", end=" => ")
        # print(str(total)+" ventas")
        # print(f"El total de ingresos que dejo este producto fue {total * price:.2f}$")
        content += f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el mes de noviembre" + " => "
        content += str(total)+" ventas\n"
        content += f"El total de ingresos que dejo este producto fue {total * price:.2f}$\n"
    
    # print("-------------------------------")
    # print("Ventas del mes de Diciembre por producto:")
    content += "-------------------------------\n"
    content += "Ventas del mes de Diciembre por producto:\n"
    for item in month_three:
        price = item[2]
        total: int = get_total(item[1])
        # print(f"El total de ventas del codigo "+item[0].replace("\n", "")+" en el mes de diciembre", end=" => ")
        # print(str(total)+" ventas")
        # print(f"El total de ingresos que dejo este producto fue {total * price:.2f}$")
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

    # print(f"El total de ventas del mes de Octubre es: {total_first_month} ventas")
    # print(f"El total de ingresos del mes de Octubre es: {total_sales_first_month:.2f}$")

    # print("-------------------------------")
    # print(f"El total de ventas del mes de Noviembre es: {total_second_month} ventas")
    # print(f"El total de ingresos del mes de Noviembre es: {total_sales_second_month:.2f}$")
    # print("-------------------------------")
    # print(f"El total de ventas del mes de Diciembre es: {total_third_month} ventas")
    # print(f"El total de ingresos del mes de Diciembre es: {total_sales_third_month:.2f}$")
    # print("-------------------------------")
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
        
        # print(f"El total de ventas del dia {day} es {len(data)} y se obtuvo una ganacia de: {total}$")
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
    content: str = ""
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
        # print("El total de ventas del codigo "+item[0], end=" => ")
        # print(str(ventas)+" ventas")
        # print(f"El total de ingresos del producto es {ventas*price:.2f}$")
        # print("-------------------------------")
        content += f"El total de ventas del codigo {item[0]} es {ventas} ventas\n"
        content += f"El total de ingresos del producto es {ventas*price:.2f}$\n"
        content += "-------------------------------\n"

    return content


def read_file(file_path_price: str, file_path_sales: str) -> str:
    with open(file_path_price, "r", encoding="utf-8") as file_price:
        content_one = file_price.readlines()

    
    with open(file_path_sales, "r", encoding="utf-8") as file_sales:
        content_two = file_sales.readlines()

    ventas, total_usd = total_of_sales(content_two=content_two, content_one=content_one)
    total_all_products: str = get_total_of_all_products(content_two=content_two, content_one=content_one)
    total_day: str = get_total_of_the_day(content_two=content_two)
    sales_month: str = sales_of_the_month(content_two=content_two, content_one=content_one)
    sales_month_product: str = sales_of_the_month_for_product(content_two=content_two, content_one=content_one)
    product_most_sold: str = get_product_most_sold(content_two=content_two, content_one=content_one)
    product_less_sold: str = get_product_less_sold(content_two=content_two, content_one=content_one)
    histogram_content: str = histogram(content_one=content_one, content_two=content_two)

    with open("reporte_de_ventas.txt", "a", encoding="utf-8") as report_file:
        report_file.write(f"El total de ventas del trimestre es: {ventas} ventas\n")
        report_file.write(f"El total de ingresos del trimestre es: {total_usd:.2f}$\n")
        report_file.write("-"*50 + "\n")
        report_file.write("El total de ventas por producto es el siguiente: \n")    
        report_file.write("-"*50 + "\n")
        report_file.write(total_all_products)
        report_file.write("-"*50 + "\n")
        report_file.write(total_day)
        report_file.write("-"*50 + "\n")
        report_file.write(sales_month)
        report_file.write("-"*50 + "\n")
        report_file.write(sales_month_product)
        report_file.write("-"*50 + "\n")
        report_file.write(product_most_sold)
        report_file.write("-"*50 + "\n")
        report_file.write(product_less_sold)
        report_file.write("-"*50 + "\n")
        report_file.write(histogram_content)
        report_file.write("-"*50 + "\n")
    # print(f"El total de ventas del trimestre es: {ventas} ventas")
    # print(f"El total de ingresos del trimestre es: {total_usd:.2f}$")
    # print("-"*50)
    # print("El total de ventas por producto es el siguiente: ")
    # get_total_of_all_products(content_two=content_two, content_one=content_one)  
    # print("-"*50)
    # get_total_of_the_day(content_two=content_two)
    # print("-"*50)
    # sales_of_the_month(content_two=content_two, content_one=content_one)
    # print("-"*50)
    # sales_of_the_month_for_product(content_two=content_two, content_one=content_one)
    # print("-"*50)
    # """En proceso"""
    # print("-"*50)
    # get_product_most_sold(content_two=content_two, content_one=content_one)
    # print("-"*50)
    # get_product_less_sold(content_two=content_two, content_one=content_one)
    # histogram(content_one=content_one, content_two=content_two)
    

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