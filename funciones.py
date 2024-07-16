import csv
import statistics
import random


trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", 
                "Elena Fernández"]


def asignar_sueldos(trabajadores):
    sueldo_aleatorios = {}
    for a in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldo_aleatorios[a] = sueldo
    return sueldo_aleatorios

def clasificar_sueldos(sueldo_aleatorios):
    menor_800 = {}
    entre_800_2m = {}
    superior_2m = {}
    
    for a, sueldo in sueldo_aleatorios.items():
        if sueldo < 800000:
            menor_800[a] = sueldo
        elif 800000 < sueldo < 2000000:
            entre_800_2m[a] = sueldo
        elif sueldo >= 2000000:
            superior_2m[a] = sueldo
    print("Sueldos menores a $800.000:", len(menor_800))
    for a, sueldo in menor_800.items():
        print("")
        print(a, ": $", sueldo)
    
    print("Sueldos entre 800.000 y 2.000.000:", len(entre_800_2m))
    for a, sueldo in entre_800_2m.items():
        print("")
        print(a, ": $", sueldo)
    
    print("Sueldos superiores a 2.000.000:", len(superior_2m))
    for a, sueldo in superior_2m.items():
        print("")
        print(a, ": $", sueldo)

def calcular_estadisticas(sueldo_aleatorios):
    sueldos = list(sueldo_aleatorios.values())

    if not sueldos:
        print("No hay sueldos asignados")
        return None, None, None, None
    descuento_salud = 0.07
    descuento_afp = 0.12
    sueldo_liquido = (sueldos)
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    media_geometrica = statistics.geometric_mean(sueldos)
    return max_sueldo, min_sueldo, promedio, media_geometrica

def generar_reporte(sueldo_aleatorios):
    with open("reportes_de_sueldos.csv", "w", newline="") as archivo:
        reporte = csv.writer(archivo, delimiter=",")
        reporte.writerow(["Nombre Trabajador", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        for trabajador, sueldo in sueldo_aleatorios.items():
            reporte.writerow([trabajador, sueldo])
        print("Reporte generado con éxito")

