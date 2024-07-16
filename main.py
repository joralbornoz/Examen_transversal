import funciones as fn


trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", 
                "Elena Fernández"]

while True:
    print("Menu")
    print("(1). Asignar Sueldos aleatorios")
    print("(2). Clasificar Sueldos")
    print("(3). Ver Estadísticas")
    print("(4). Generar Reporte de Sueldos")
    print("(5). Salir")
    try:
        opc = int(input("Seleccione Opcion: "))

        if opc == 1:
            sueldo_aleatorios = fn.asignar_sueldos(trabajadores)
        elif opc == 2:
            fn.clasificar_sueldos(sueldo_aleatorios)
        elif opc == 3:
            max_sueldo, min_sueldo, promedio, media_geometrica = fn.calcular_estadisticas(sueldo_aleatorios)
            if promedio is not None:
                print("Sueldo máximo: \n", max_sueldo)
                print("Sueldo mínimo: \n", min_sueldo)
                print("Promedio de sueldos: \n", promedio)
                print("Media geométrica de sueldos: \n", media_geometrica)
        elif opc == 4:
            fn.generar_reporte(sueldo_aleatorios)
        elif opc == 5:
            print("Finalizando Programa...")
            print("Desarrollado por Jorge Albornoz")
            print("Rut: 16.912.006-4")
            break
        else:
            print("Opción inválida. Seleccione una opción del 1 al 5.")
    
    except ValueError:
        print("Opción debe ser un número del 1 al 5.")





























