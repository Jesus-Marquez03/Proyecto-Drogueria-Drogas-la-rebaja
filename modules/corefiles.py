import json

#CON ESTA FUNCION LLAMAMOS A LOS ARCHIVOS JSON 

def cargarMedicamentos(ruta):

    with open(ruta, "r", encoding="utf-8") as datosMed:

        datosMedicamentos = json.load(datosMed)

    return datosMedicamentos

def cargarProveedores(ruta):

    with open(ruta, "r", encoding="utf-8") as datosProve:

        datosProveedores = json.load(datosProve)

    return datosProveedores

def cargarCompras(ruta):

    with open(ruta, "r", encoding="utf-8") as datosComp:

        datosCompras = json.load(datosComp)

    return datosCompras

def cargarEmpleados(ruta):

    with open(ruta, "r", encoding="utf-8") as datosEmple:

        datosEmpleados = json.load(datosEmple)

    return datosEmpleados

def cargarVentas(ruta):

    with open(ruta, "r", encoding="utf-8") as datosVen:

        datosVentas = json.load(datosVen)

    return datosVentas

def cargarPacientes(ruta):

    with open(ruta, "r", encoding="utf-8") as datosPac:

        datosPacientes = json.load(datosPac)

    return datosPacientes