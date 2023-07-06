import funciones as fn
nombre_funcionario =input ("ingrese su nombre de funcionario")
    
                       
while True:
    fn.menu()
    opc = fn.validar_opcion()
    if opc== 1:
        fn.comprar()
    elif opc == 2:
        ubicacion = fn.mostrar_ubicaciones()
    elif opc == 3:
        pass
    elif opc == 4:
        ganancias = fn.ganancias_totales()
    elif opc == 5:
        print ("finalizo el programa",nombre_funcionario)
        
        break
