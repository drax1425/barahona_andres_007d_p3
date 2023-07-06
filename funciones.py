import numpy as np
import os
# time.slip ()
import time
def fecha_inicio():
    while True:
        try:
            fecha_inicio = int(input("ingrese la fecha que prendio el programa: "))
            if fecha_inicio == "-":
                return fecha_inicio
            else:
                print ("ingrese su fecha con -")
        except:
            print("ingrese numeros enteros ")
escenario = np.zeros((10,10),int)
lista_numeros=(1,2,3,4,5,6,7,8,9,10)
lista_letras = ["A B C D E F G H I J"]
platino =120000
gold = 80000
silver = 50000
lista_ruts = []
lista_filas = []
lista_columnas = []
def menu():
    print("""Menu:
    |-------------------------------------------|
    |        1.Comprar entrada                  |
    |-------------------------------------------|
    |        2.Mostrar ubicaciones              |
    |-------------------------------------------|
    |        3.Ver listado de asistentes        |
    |-------------------------------------------|
    |        4.Mostrar ganancias totales        |
    |-------------------------------------------|
    |    5.Salir                                |
    |-------------------------------------------|""")

def validar_opcion():
    while True:
        try:
            opc =int (input("    ingrese una de las opciones: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ingrese una de las 5 opciones dadas")
        except:
            print("ingrese numeros enteros")

#mostrar ubicacion 
def mostrar_ubicaciones(): 
    print("        A B C D E F G H I J")
    for x in range(10):
        print("fila",lista_numeros[x],end="\t")
        for y in range (10):
            print(escenario[x][y],end=" ")
        print()
def validar_rut():
    while True:
        try:
            rut = int(input("ingrese su rut sin numeros verificador ni puntos: "))
            if rut >10000000 and rut <99999999:
                return rut
            else:
                print("ingrese el rut sin numero verificador ni puntos")
        except:
            print("ingrese solo numeros enteros ")
def validar_tipo_entrada ():
    while True:
        try:
            entrada = int (input("que entrada desa: "))
            if entrada in (1,2,3):
                return entrada
            else:
                print("solo puede unas de las 3 opciones")
        except:
            print("ingrese numeros enteros")
def validar_cantidad_platino ():
    while True:
        try:    
                cantidad_platino =int(input("ingrese la cantidad 1 a 3: "))
                if cantidad_platino in (1,2,3):
                    return cantidad_platino
                else:
                    print("Solo puede comprar hasta 3 entradas")
        except:
            print("ingrese numeros enteros")
def validar_cantidad_gold():
    while True:
        try:    
            cantidad_gold =int(input("ingrese la cantidad 1 a 3: "))
            if cantidad_gold in (1,2,3):
                return
            else:
                print("Solo puede comprar hasta 3 entradas")
        except:
            print("ingrese numeros enteros")
def validar_cantidad_silver():
    while True:
        try:    
            cantidad_silver =int(input("ingrese la cantidad 1 a 3: "))
            if cantidad_silver in (1,2,3):
                return
            else:
                print("Solo puede comprar hasta 3 entradas")
        except:
            print("ingrese numeros enteros")
def comprar():
    print(f"""tipo entrada:
    1.Platinum {platino} (fila 1 y 2)
    2.Gold     {gold}  (fila 3 a 5)
    3.Silver   {silver}  (fila 6  a 10)""")
    
    entrada = validar_tipo_entrada()
    if entrada ==1:
        cantidad_platino = validar_cantidad_platino()
        total_platino = cantidad_platino * platino
        print(f"Su total a pagar es {total_platino}")
    elif entrada == 2:
        cantidad_gold = validar_cantidad_gold()
        total_gold = cantidad_gold * gold
        print(f"Su total a pagar es {total_gold}")
    elif entrada == 3:
        cantidad_silver = validar_cantidad_silver()
        total_silver = cantidad_silver * silver
        print(f"Su total a pagar es {total_silver}")
    
    mostrar_ubicaciones()
    if 0 not in escenario:
        print("No quedan reservas")
    fila = input ("ingrese la su fila: ")
    columna = input ("ingrese la letra de la columna: ")
    
      
    rut = validar_rut()
    lista_ruts.append(rut)
    lista_filas.append(fila)
    lista_columnas.append(columna)

#opcion 4 
def ganancias_totales():
    print(f"""Tipo entrada | Cantidad | Total
Platinum $ {platino} |    """)
