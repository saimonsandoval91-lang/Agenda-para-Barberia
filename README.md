# Agenda-para-Barberia
Desarrollador del Sistema de Control de Citas (Proyecto Independiente)  Creación de un software en Python para la administración de flujos de trabajo en una barbería, aplicando conceptos avanzados de los módulos Cisco Python 1 y 2.
Este es un sistema de gestion integral desarrollado en Python para la administracion de citas, clientes y empleados de una barberia profesional. El proyecto demuestra la aplicacion de logica de programacion y el uso de estructuras de datos para resolver problemas de organizacion en un negocio real.

Funcionalidades Principales
Gestion de Citas (CRUD): Permite crear, leer, actualizar y eliminar citas de forma dinamica.

Registro de Clientes y Empleados: Modulos independientes para el control de datos personales con validacion de identidad unica por medio de la Cedula.

Validacion de Datos: Uso de logica para asegurar que nombres, telefonos y correos electronicos cumplan con el formato correcto antes de ser guardados.

Persistencia de Datos: Los registros se almacenan en archivos de texto (.txt), lo que permite que la informacion se mantenga guardada aun despues de cerrar el programa.

Sistema de Backups: Generacion automatica de copias de seguridad en una carpeta dedicada, utilizando marcas de tiempo para evitar la perdida de informacion importante.

Tecnologias y Conceptos Aplicados
Lenguaje: Python.

Paradigma: Programacion Orientada a Objetos (OOP) mediante el uso de clases para representar Clientes y Empleados.

Librerias Estandar utilizadas:

os: Para la gestion de rutas y verificacion de archivos en el sistema.

shutil: Para la creacion de los respaldos de seguridad (backups).

datetime: Para el manejo de fechas en la agenda y nombres de los archivos de respaldo.

ast: Para la lectura y conversion segura de datos almacenados en los archivos de texto.

Estructura del Codigo
main.py: Punto de entrada principal con el menu para la gestion de clientes.

mainagenda.py: Modulo dedicado exclusivamente a la operacion de la agenda de citas.

mainempleads.py: Interfaz para el control de los registros de trabajadores.

Classecliente.py y classempleado.py: Definicion de las clases y sus metodos de captura de datos.

modulodeFunciones.py y modulosdefuncionesempleados.py: Contienen la logica de procesamiento, busqueda y persistencia de datos.

Como ejecutar el proyecto
Descargar los archivos del repositorio.

Contar con un interprete de Python instalado en el equipo.

Ejecutar el archivo main.py para iniciar el sistema
