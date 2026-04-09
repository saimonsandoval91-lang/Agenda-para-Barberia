from funciones_agenda import *

def menu_agenda():
    while True:
        print("\n" + "="*40)
        print("        AGENDA DE CITAS")
        print("="*40)
        print("1. Agregar cita")
        print("2. Ver todas las citas")
        print("3. Buscar cita")
        print("4. Modificar cita")
        print("5. Eliminar cita")
        print("6. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            guardar_cita()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            buscar_cita()
        elif opcion == "4":
            modificar_cita()
        elif opcion == "5":
            eliminar_cita()
        elif opcion == "6":
            print("Saliendo de agenda...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_agenda()