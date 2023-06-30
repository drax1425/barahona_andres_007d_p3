import funciones as fn

while True:
    print("""MENU DE OPCIONES: 
    1.Grabar:
    2.Buscar 
    3.Retirarse
    4.Salir""")
    opc = fn.validar_opcion()
    if opc == 1:
        fn.registrar()
    elif opc ==2:
        fn.buscar()
    elif opc == 3:
       pass
    elif opc == 4:
        fn.salir()