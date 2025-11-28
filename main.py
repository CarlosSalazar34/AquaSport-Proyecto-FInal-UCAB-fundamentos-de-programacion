import os

def total_of_sales(content: str) -> int:
    total: int = 0

    for line in content[1::]:
        data = line[1:-1].split(",")
        for price in data[1::]:
            total += int(price)
    return total



def read_file(file_path_price: str, file_path_sales: str) -> str:
    # os.system("cls")
    with open(file_path_price, "r", encoding="utf-8") as file_price:
        content_one = file_price.readlines()

    
    with open(file_path_sales, "r", encoding="utf-8") as file_sales:
        content_two = file_sales.readlines()


    total: int = total_of_sales(content=content_two)

    print(f"El total de ventas del trimestre es: {total}")

    temp_columns = content_two[0].split(",")
    columns = []
    i = 1
    while i < len(temp_columns):
        columns.append(temp_columns[i].strip())
        i += 1

    ventas_totales_lista = []
    i = 0
    while i < len(columns):
        ventas_totales_lista.append(0)
        i += 1

    # Lógica de Acumulación de Ventas
    for j in range(1, len(content_two)): 
        
        temp_data = content_two[j].split(",")
        data = []
        
        v = 1
        while v < len(temp_data):
            data.append(temp_data[v].strip().replace('\n', ''))
            v += 1
            
        for v in range(len(data)):
            cantidad_vendida = int(data[v])
            cantidad_vendida = 0
            
            ventas_totales_lista[v] += cantidad_vendida
    
    print("\n--- 📊 Reporte de Unidades Vendidas por Producto ---")
    
    for i in range(len(columns)):
        print(f"📦 El total de ventas del producto **{columns[i]}** es: **{ventas_totales_lista[i]} unidades**")
    
    print("\n**Fin del Reporte**")


    # columns: list[int] = []

    # for i in content_two[0].split(",")[1::]:
    #     columns.append(i)

    # print(columns)
    # print(len(columns))
    # print(columns)
    # print(len(columns))            
    # for item in content_two[::]:
    #     data = item.split(",")[1::]
    #     print(data)
    #     print(len(data))

    # print(content_two)

    # for i in range(0, len(columns)):
    #     for j in range(1, len(content_two)):
    #         # print(content_two[j], end=" ")
    #         data = content_two[j].split(",")[1::]
    #         # print(data)
    #         # print(len(data))
    #         for v in (0, len(data)):
    #             if i == v:
    #                 print(f"El total de ventas del producto {columns[i]} es: {data[v]}")
            # print(data)
            # if i == j:
                # print(f"El total de ventas del producto {columns[i]} es: {data[j]}")

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