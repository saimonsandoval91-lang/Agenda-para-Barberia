import os
import ast

class Agenda:
    def __init__(self):
        self.archivo_agenda = "agenda.txt"
        self.archivo_clientes = "registros_clientes.txt"
        self.archivo_empleados = "registros_empleados.txt"
    
    def cargar_clientes(self):
        clientes = []
        if os.path.exists(self.archivo_clientes):
            with open(self.archivo_clientes, "r", encoding="utf-8") as archivo:
                contenido = archivo.read().strip()
                if contenido:
                    try:
                        lista_clientes = ast.literal_eval(contenido)
                        for cliente in lista_clientes:
                            clientes.append({
                                "nombre": cliente["Nombre"],
                                "cedula": cliente["Cedula"]
                            })
                    except:
                        print("Error al leer clientes")
        return clientes
    
    def cargar_empleados(self):
        empleados = []
        if os.path.exists(self.archivo_empleados):
            with open(self.archivo_empleados, "r", encoding="utf-8") as archivo:
                contenido = archivo.read().strip()
                if contenido:
                    try:
                        lista_empleados = ast.literal_eval(contenido)
                        for empleado in lista_empleados:
                            empleados.append({
                                "nombre": empleado["empleado"],
                                "cedula": empleado["Cedula"]
                            })
                    except:
                        print("Error al leer empleados")
        return empleados
    
    def cliente_existe(self, nombre_cliente):
        clientes = self.cargar_clientes()
        for cliente in clientes:
            if cliente["nombre"].lower() == nombre_cliente.lower():
                return True
        return False
    
    def empleado_existe(self, nombre_empleado):
        empleados = self.cargar_empleados()
        for empleado in empleados:
            if empleado["nombre"].lower() == nombre_empleado.lower():
                return True
        return False