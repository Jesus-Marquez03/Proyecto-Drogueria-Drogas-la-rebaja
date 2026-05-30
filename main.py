from modules.farmacia import verMedicamentos
from modules.farmacia import verEmpleados
from modules.farmacia import verPacientes
from modules.farmacia import verProveedores

import os 
def mainMenu():
    return ["1. Gestión Farmacia","2. Ventas y Compras","3. Generador de Informes","4. Reportes Avanzados","5. Salir"]
def mainMedicamentos():
    return ["1. Ver medicamentos","2. Ver proveedores","3. Ver clientes","4. Ver empleados","0. Volver"]

while True:
    try:
        os.system('cls')
        print("================== FARMACIA ================== ")
        for item in mainMenu():
            print(item)
        opMenu = int(input("Ingrese una de las opciones: "))
        break
    except ValueError: 
        print("Ingrese una opción valida")
        x = input("Presione enter para continuar....")
match opMenu:
    case 1:
        while True:
            try:
                os.system('cls')
                print("==================== GESTION FARMACIA ===================")
                for item in mainMedicamentos():
                    print(item)
                opGestionFar = int(input("Ingrese una de las opciones: "))
            except ValueError:
                print("Ingrese una opción valida")
            match opGestionFar:
                case 1:
                    verMedicamentos()
                    x = input("Presione enter para continuar....")
                case 2:
                    verProveedores()
                    x = input("Presione enter para continuar....")
                case 3:
                    verPacientes()
                    x = input("Presione enter para continuar....")
                case 4:
                    verEmpleados()
                    x = input("Presione enter para continuar....")
                case 5:
                    break
                case _:
                    print("Ingrese una opción valida")
                    x = input("Presione enter para continuar....")
    case 2:
        pass
    case 3:
        pass
    case 4:
        pass
    case 5:
        pass
    case _:
        print("Ingrese una opción valida")