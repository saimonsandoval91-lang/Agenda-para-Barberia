#Clase cita del salon de belleza
import re
from datetime import datetime # esto lo que hace es ayudarnos dando fechaas exactas para tener un seguimiento
class Cita:
    def __init__(self):
        self.__datos = {"Nombre":"","Cedula":0,"numero":0,"correo":""}
    def registro (self):
        #En este punto se hacen las partes de los registros para la
        while True:
            nombrox= input ("Ingrese su nombre:\n→ ")#esto es para registrar el nombre unicamnete en datos
            if  nombrox.isalpha():
                self.__datos["Nombre"] = nombrox
                break
            else:
                print("No puedes digitar numeros en el nombre")
        while True:
            ceduls= input("Ingrese su Cedula:\n→ ")
            if ceduls.isdigit():
                self.__datos["Cedula"] = ceduls
                break
            else:
                print("Solo puedes digitar numeros en la cedula")

        
        while True:
            correo = input("Por favor digite el correo del usuario con su @\n→")
            if "@" in correo:
                self.__datos["correo"]= correo
                break
            else:
                print("su correo le hace falta un arroba")

        while True:
            num= input("Ingrese su numero telefonico:\n→ ")
            if num.isdigit():
                self.__datos["numero"] = num
                break
            else:
                print("Solo puedes digitar numeros para el telefono")


    def to_dict(self):#este def lo que hace es guardar los datos en la lista
        return self.__datos   
     
    def __str__(self):#este str lo que hace es ver los daatos de la lista de manera legible
        return self.__datos