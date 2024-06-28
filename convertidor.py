def menu_principal():
    print("1. Convertir Peso")
    print("2. Convertir Temperatura")
    print("3. Convertir Distancia")
    print("4. Salir")


def menu_peso():
    print("1. de gr. a kg.")
    print("2. de kg. a gr.")
    print("3. de kg. a Tons.")
    print("4. de Tons. a kg.")
    print("5. Salir")


def menu_temperatura():
    print("1. de Celcius a Farenheit")
    print("2. de Farenheit a Celcius")
    print("3. Salir")


def menu_distancia():
    print("1. de Metros a Km.")
    print("2. de Km. a Metros")
    print("3. de Km. a Millas")
    print("4. de Millas a Km")
    print("5. Salir")


def bienvenida():
    print("Bienvenido al Conversor V 1.0")
    print("Creado por Gabriel Guerra")
    print("Fecha 12 de Jun de 2024")
    print(" ")


def convertidor():
    bienvenida()
    while True:
        unidad1 = int(input("Ingresa una cantidad: "))
        print(" ")
        multi = unidad1 * 1000
        divi = unidad1 / 1000
        miles_to_km = unidad1 * 1.609
        km_to_miles = unidad1 / 1.609
        far_to_cel = (unidad1 - 32) * (5 / 9)
        cel_to_far = (unidad1 * (9 / 5) + 32)
        menu_principal()
        op = str(input("Selecciona una operacion: "))
        print(" ")
        if op == "1":
            menu_peso()
            peso = input("Selecciona el tipo de conversion: ")
            print(" ")
            if peso == "1":
                print(f"{unidad1} gr. equivalen a {divi} kg.")
            elif peso == "2":
                print(f"{unidad1} kg. equivalen a {multi} gr.")
            elif peso == "3":
                print(f"{unidad1} kg. equivalen a {divi} tons.")
            elif peso == "4":
                print(f"{unidad1} tons. equivalen a {multi} kg.")
            elif peso == "5":
                print("Saliendo...")
                break
            else:
                print("Seleccion Invalida!")
                break
        elif op == "2":
            menu_temperatura()
            temp = input("Selecciona el tipo de conversion: ")
            print(" ")
            if temp == "1":
                print(f"{unidad1} C° a {cel_to_far} F°")
            elif temp == "2":
                print(f"{unidad1} F° equivalen a {far_to_cel} C°")
            elif temp == "3":
                print("Saliendo...")
                break
            else:
                print("Seleccion Invalida!")
                break
        elif op == "3":
            menu_distancia()
            dist = input("Selecciona el tipo de conversion: ")
            print(" ")
            if dist == "1":
                print(f"{unidad1} mts. equivalen a {divi} Km.")
            elif dist == "2":
                print(f"{unidad1} Km. equivalen a {multi} mts.")
            elif dist == "3":
                print(f"{unidad1} Km. equivalen a {km_to_miles} Mill.")
            elif dist == "4":
                print(f"{unidad1} Mill. equivalen a {miles_to_km} Km.")
            elif dist == "5":
                print("Saliendo...")
                break
            else:
                print("Seleccion Invalida!")
                break
        elif op == "4":
            print("Saliendo...")
            break
        else:
            print("Seleccion Invalida!")
            break


convertidor()
