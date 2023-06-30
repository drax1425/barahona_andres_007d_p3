import numpy as np
import time
cuarto = np.zeros(5,int)
lista_ruts = ()
lista_nombre_mascota =()
lista_nombre = ()
lista_habitacion = (1,2,3,4,5,6,7,8,9,10)
acumulador = 0
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def validar_nombre_mascota():
    while True:
        nom_mascota = input("Ingrese nombre de su mascota: ")
        if len(nom_mascota.strip()) >= 3 and nom_mascota.isalpha():
            return nom_mascota
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def dias_en_guarderia():
    try:
        dias_guarderia= int(input("ingrese la cantidad de dias : "))
    except:
        print("ingrese solo numeros enteros")
    acumulador = acumulador + dias_guarderia
    total = acumulador *15000
    print(f"su total a pagar es {total}")
    


def salir():
    print("gracias por confiar en nosotros ")
    time.time(2)
    exit()
    
def buscar():
    ruts = input("ingrese su rut para buscar su mascota: ")
    if ruts == lista_ruts:
        print("su mascota si esta ")
    else:
        print("no estas registrado")



def registrar():
    rut = validar_rut()
    nom= validar_nombre()
    nom_mascota= validar_nombre_mascota ()
    dias_guarderia = dias_en_guarderia()
    print(cuarto)
    lista_ruts.index = rut
    lista_nombre_mascota.index = nom_mascota
    lista_nombre.index = nom
