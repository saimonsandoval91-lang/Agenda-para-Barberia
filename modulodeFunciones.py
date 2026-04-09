
#modulo de funciones

#librerias que se necesitan
import shutil #esta libreria nos ayudara a crear un respaldo y una copia de seguridad al final del dia para no depender unicamente de una sola copia de los datos
from datetime import datetime # esto lo que hace es ayudarnos dando fechaas exactas para tener un seguimiento
import json
import os
import ast

from Classecliente import * 

#variables para que el programa cumpla su funcion
registro = []

def crearDB (registro):
    try:
        archivo=open("registros_clientes.txt","w")#primero ponemos el nombre del archivo y extension y se le da el prermiso w para escribir
        archivo.write(str(registro))#esto lo que hace es crear el archivo txt de manera correcta
        print("su archivo se guardo correctamente")#avisa que se creo de manera correcta
        archivo.close()
    except:
        print("tuvimos un error")


def registrar_cliente():#
    datos = ver_registro()#esto lo que hace es llamar una funcion que se encuenta mas adelante
    pers = Cita()#esto lo que hace es ejecutar la clase para recolectar los datos del cliente
    pers.registro()#esto hace llamaar la funcion anterior haciendo que todo se termine de almacenar en la clase
    nuevo_cliente = pers.to_dict()#esto hace que se guarde en un dicionario
    for registro in datos:#aca hacemos la comprabacion de datos para evitar que se repita una cedula
        if registro["Cedula"]== nuevo_cliente["Cedula"]:#en esta linea se comprueba que no  se encuentren la cedula ingresada con una anterior que siga presente
            print("la cedula ya se encuentra en el sistema ")
            return
    datos.append(nuevo_cliente)#si no se encuentra la cedula se logra registrar en el sistema
    crearDB(datos)#esto lo que hace es llamar a la funcion de crearDB y mandarlo a datos


def ver_registro ():#esta funcion lo que hace es leer los datos de la listra mostrandolo al empleado para que este vea la lista con los datos
     if os.path.exists ("registros_clientes.txt"):#esto lo que hace es cuando la lista esta creada muestre los datos
         registro = open("registros_clientes.txt","r")#con esa r se le da el permiso para leer el txt y mostrarlo
         datos = registro.read()#en esta lista hace que datos se lean en el sistema
         registro.close()#cierra el registro para detener que siga leyendo
         lista = ast.literal_eval(datos)#hace que lista sean la lista de manera visual al usuario para que se pueda leer de manera logica y visual
         return lista#devuelve la lista al empleado para que el la lea
     return []


def buscar ():#esto hace que con el numero de cedula se pueda encontrar todos los datos de la lista del cliente
    registro = ver_registro()
    buscarcedula = int(input("digite la cedula que desea buscar"))#para ingresar la cedula
    for x in registro:#esto es para comprobar que este en el registro
        encontrado= True#si esta
        if buscarcedula == x["Cedula"]:
            print("datos encontrados")
            print(x)#se muestran los datos
        else:
            encontrado=False#si se mantiene en falso osea que no estan eso significa que esta misma no esta
    if encontrado == False:
        print("datos no encontrado o no registrados")
    

def modf():#esta funcion sirve para modificar los datos del dicionario
    registro=ver_registro()#para ver el registro
    buscarcedula = int(input("digite la cedula que desea buscar\n→"))#para que el empleado digite la cedulaa
    for x in registro:
        encontrado= True#si se mantiene asi dejara que coontinuen los otros pasos
        if buscarcedula == x ["Cedula"]:#esto hace que la cedula sea igual 
            print("estos son sus datos",x)
            opcion= int(input('''
1-modificar el Nombre
2-modificar servicio
3-Cambio de hora
4-cambio de fecha
 → '''))#aca se muestran las opciones de cambio
            if opcion == 1:#deja cambiar el nombre
                nuevonombre= input("digite el nuevo nombre")
                x["Nombre"]=nuevonombre
                crearDB(registro)
            if opcion == 2:#deja cambiar el servicio
                nuevoservicio= input("digite el nuevo nombre")
                x["servicio"]=nuevoservicio
                crearDB(registro)
            if opcion == 3:#deja dar una nueva hora
                nuevahora= input("digite el nuevo nombre")
                x["hora"]=nuevahora
                crearDB(registro)
            if opcion == 4:
                nuevafecha= int(input("digite la nueva fecha (ddmmaaaa)"))
                x["Fecha"]=nuevafecha
            print("archivo modificado")

        else:
            encontrado = False
    if encontrado== False:
        print("dato no encontrado,no se puede modificar")



def elim ():
    registro = ver_registro()#esto ve el registo
    buscarcedula=int(input("digite la Cedula que desea eliminar"))#esto es para que el empleado busque la cedula del cliente
    encontrado = False#si no la encuentra es falso
    for x in registro:
        if buscarcedula == x["Cedula"]:#aca busca la cedula si es igual a la base de datos
            print("Se encontraron los datos")#aca se encuentra la cedula
            print (x)#muestra los datos solicitados de x
            elimdato= registro.index(x)#elimina los datos de x en el registro
            del registro [elimdato]#los saca del txt
            print ("Se elimino el dato")#da aviso a la eliminacion de datos
            crearDB(registro)#aca guarda el registro en la base de datos oseaa el txt
            encontrado = True#este true hace que se rompa el true en breaak
            break
    if not encontrado:#si el encontrado se encuentra en False aun despuues de ingresar la cedula dara el mensaje de no encontrada
            print("no se encontro la Cedula")


def backup():#hace un respaldo de los archivos cada vez que se sale del sistema
    carp = "backup"#esto es ek nombre de la carpetal
    if not os.path.exists(carp):#si no esta la carpeta la crea
        os.makedirs(carp)#esto haace que se cree la carpeta
    if not os.path.exists("registros_clientes.txt"):#si esa carpeta existe devuelve lo siguiente
        return
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M")#fecha y hora en el txt
    nombredelrespaldo = f"{carp}/backup_{fecha}.txt"
    shutil.copy("registros_clientes.txt", nombredelrespaldo)#hace una copia dentro de la carpeta con nombre de backup
    print(f"Copia de seguridad creada en: {nombredelrespaldo}")#esto muestra la ubicacion donde se guardo el archivo

