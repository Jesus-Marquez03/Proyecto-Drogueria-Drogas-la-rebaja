from .corefiles import cargarMedicamentos
from .corefiles import cargarProveedores
from .corefiles import cargarPacientes
from .corefiles import cargarEmpleados

def verMedicamentos():
    medicamentos = cargarMedicamentos(
         "data/medicamentos.json"
        )
    for medicamento in medicamentos:
        for item, value in medicamento.items():
            print(f"{item},{value}")
        print("-" * 74)

def verProveedores():
    proveedores = cargarProveedores(
         "data/proveedores.json"
        )
    for proveedor in proveedores:
        for item, value in proveedor.items():
            print(f"{item},{value}")
        print("-" * 74)

def verPacientes():
    pacientes = cargarPacientes(
         "data/pacientes.json"
        )
    for paciente in pacientes:
        for item, value in paciente.items():
            print(f"{item},{value}")
        print("-" * 74)

def verEmpleados():
    empleados = cargarEmpleados(
         "data/empleados.json"
        )
    for empleado in empleados:
        for item, value in empleado.items():
            print(f"{item},{value}")
        print("-" * 74)