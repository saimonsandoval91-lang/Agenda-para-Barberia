import os
from class_agenda import Agenda

def guardar_cita():
    agenda = Agenda()
    print("\n--- AGREGAR CITA ---")
    
    cliente = input("Nombre del cliente: ")
    if not agenda.cliente_existe(cliente):
        print("El cliente no está registrado")
        return
    
    servicio = input("Servicio: ")
    fecha = input("Fecha (dd/mm/aaaa): ")
    hora = input("Hora: ")
    empleado = input("Empleado: ")
    
    if not agenda.empleado_existe(empleado):
        print("El empleado no está registrado")
        return
    
    with open("agenda.txt", "a") as archivo:
        archivo.write(f"{cliente},{servicio},{fecha},{hora},{empleado}\n")
    
    print("Cita guardada!")

def ver_citas():
    print("\n--- TODAS LAS CITAS ---")
    
    if not os.path.exists("agenda.txt"):
        print("No hay citas")
        return
    
    with open("agenda.txt", "r") as archivo:
        citas = archivo.readlines()
    
    if not citas:
        print("No hay citas")
    else:
        for i, cita in enumerate(citas, 1):
            datos = cita.strip().split(",")
            if len(datos) >= 5:
                print(f"{i}. Cliente: {datos[0]}")
                print(f"   Servicio: {datos[1]}")
                print(f"   Fecha: {datos[2]} Hora: {datos[3]}")
                print(f"   Empleado: {datos[4]}")
                print()

def buscar_cita():
    print("\n--- BUSCAR CITA ---")
    
    if not os.path.exists("agenda.txt"):
        print("No hay citas")
        return
    
    nombre = input("Buscar por nombre de cliente: ")
    
    with open("agenda.txt", "r") as archivo:
        citas = archivo.readlines()
    
    encontradas = 0
    for cita in citas:
        datos = cita.strip().split(",")
        if len(datos) >= 5 and nombre.lower() in datos[0].lower():
            print(f"Cliente: {datos[0]}")
            print(f"Servicio: {datos[1]}")
            print(f"Fecha: {datos[2]} Hora: {datos[3]}")
            print(f"Empleado: {datos[4]}")
            print("-" * 20)
            encontradas += 1
    
    if encontradas == 0:
        print("No se encontraron citas")

def modificar_cita():
    agenda = Agenda()
    print("\n--- MODIFICAR CITA ---")
    
    ver_citas()
    
    if not os.path.exists("agenda.txt"):
        return
    
    try:
        with open("agenda.txt", "r") as archivo:
            citas = archivo.readlines()
        
        if not citas:
            print("No hay citas para modificar")
            return
        
        numero = int(input("Número de cita a modificar: ")) - 1
        
        if 0 <= numero < len(citas):
            datos = citas[numero].strip().split(",")
            
            print(f"\nCita actual:")
            print(f"1. Servicio: {datos[1]}")
            print(f"2. Fecha: {datos[2]}")
            print(f"3. Hora: {datos[3]}")
            print(f"4. Empleado: {datos[4]}")
            
            opcion = input("\n¿Qué quieres modificar? (1-4): ")
            
            if opcion == "1":
                nuevo = input(f"Nuevo servicio [{datos[1]}]: ") or datos[1]
                datos[1] = nuevo
            elif opcion == "2":
                nuevo = input(f"Nueva fecha [{datos[2]}]: ") or datos[2]
                datos[2] = nuevo
            elif opcion == "3":
                nuevo = input(f"Nueva hora [{datos[3]}]: ") or datos[3]
                datos[3] = nuevo
            elif opcion == "4":
                nuevo = input(f"Nuevo empleado [{datos[4]}]: ") or datos[4]
                if not agenda.empleado_existe(nuevo):
                    print("El empleado no está registrado")
                    return
                datos[4] = nuevo
            else:
                print("Opción inválida")
                return
            
            citas[numero] = f"{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]}\n"
            
            with open("agenda.txt", "w") as archivo:
                archivo.writelines(citas)
            
            print("Cita modificada!")
        else:
            print("Número inválido")
            
    except ValueError:
        print("Error: ingrese un número válido")

def eliminar_cita():
    print("\n--- ELIMINAR CITA ---")
    
    ver_citas()
    
    if not os.path.exists("agenda.txt"):
        return
    
    try:
        with open("agenda.txt", "r") as archivo:
            citas = archivo.readlines()
        
        if not citas:
            print("No hay citas para eliminar")
            return
        
        numero = int(input("Número de cita a eliminar: ")) - 1
        
        if 0 <= numero < len(citas):
            datos = citas[numero].strip().split(",")
            
            print(f"Cita a eliminar:")
            print(f"Cliente: {datos[0]}")
            print(f"Servicio: {datos[1]}")
            
            confirmar = input("¿Eliminar? (s/n): ").lower()
            
            if confirmar == 's':
                citas.pop(numero)
                
                with open("agenda.txt", "w") as archivo:
                    archivo.writelines(citas)
                
                print("Cita eliminada!")
            else:
                print("Cancelado")
        else:
            print("Número inválido")
            
    except ValueError:
        print("Error: ingrese un número válido")