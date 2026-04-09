# main: menú para que el empleado pueda registrar al cliente

import modulodeFunciones as MF

opcion = 0
try:
    while opcion != 6:

            opcion = int(input('''
Bienvenido al sistema de citas de la Barberia Gran Master
digite la opcion que desea usar para ayudar al cliente
1 - Insertar datos
2 - Leer archivo
3 - Buscar
4 - Modificar
5 - Eliminar
6 - Salir
→ '''))

            if opcion == 1:
                MF.registrar_cliente()
            elif opcion == 2:
                print(MF.ver_registro())
            elif opcion == 3:
                print("Buscando...")
                MF.buscar()
            elif opcion == 4:
                print("Modificar")
                MF.modf()
            elif opcion == 5:
                print("Eliminar")
                MF.elim()
            elif opcion == 6:
                print("Saliendo...")
                MF.backup()
            else:
                print("Opción inválida")
except:
    print("tuvimos un errror al introducir los datos")

# Al salir del bucle, también se asegura un backup final
MF.backup()