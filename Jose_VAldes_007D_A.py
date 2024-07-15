from os import system
import csv
import random


trabajadores=[{"Nombre": "Juan Perez", "Sueldo": None}, {"Nombre": "Maria Garcia", "Sueldo": None}, {"Nombre": "Carlos Lopez", "Sueldo": None}, {"Nombre": "Ana Martinez", "Sueldo": None}, {"Nombre": "Pedro Rodriguez", "Sueldo": None}, {"Nombre": "Laura Fernandez", "Sueldo": None}, {"Nombre": "Miguel Sanchez", "Sueldo": None}, {"Nombre": "Isabel Gomez", "Sueldo": None}, {"Nombre": "Francisco Diaz", "Sueldo": None}, {"Nombre": "Elena Fernandez", "Sueldo": None}]

def Asignar_Sueldos():
    for trabajador in trabajadores:
        trabajador["Sueldo"]=random.randint(300000,2500000)
        print(f"trabajador {trabajador["Nombre"]} con sueldo {trabajador["Sueldo"]}")

def Clasificar_Sueldos():
    contador=0
    contador1=0
    contado2=0
    Total=0
    for trabajador in trabajadores:
        if trabajador["Sueldo"] is None:
            print("Trabajadores no poseen sueldo")
            return
    
    print("Nombre Empleado", "Sueldo")
    
    for trabajador in trabajadores:
        if trabajador["Sueldo"]< 800000:
         print(f"{trabajador["Nombre"]}, {trabajador["Sueldo"]}")
         contador+=1
         contador=contador
         Total+=trabajador["Sueldo"]
    print(f"Sueldos menores a $800000 Total:{contador}")
    print()
    print("Nombre Empleado", "Sueldo")
    
    for trabajador in trabajadores:
        if trabajador["Sueldo"]>=800000 and trabajador["Sueldo"]<=2000000:
            print(f"{trabajador["Nombre"]}, {trabajador['Sueldo']}")
            contador1+=1
            contador1=contador1 
            Total+=trabajador["Sueldo"]
    print(f"Sueldos entre $800000 y $2000000 Total:{contador1}")           
    print()
    print("Nombre Empleado", "Sueldo")
    
    for trabajador in trabajadores:
        if trabajador["Sueldo"]>2000000:
            print(f"{trabajador["Nombre"]}, {trabajador['Sueldo']}")
            contado2+=1
            contado2=contado2
            Total+=trabajador["Sueldo"]
    print(f"Sueldos superiores a $2000000 Total:{contado2}")       
    print()
    print()
    print(f"Sueldos Totales: ${Total}")

def Ver_Estadistica():
    promedio=0
    total=0
    for trabajador in trabajadores:
       if trabajador["Sueldo"] is None:
           print("Trabajadores no poseen sueldo")
           return
    
    for trabajador in trabajadores:
       
        promedio+=trabajador["Sueldo"]
        total+=promedio
    sueldo=round(total/len(trabajadores))    
    print(f"Promedio sueldo ${sueldo}")
         

   
def Reporte_sueldos():

    for trabajador in trabajadores:
        if trabajador["Sueldo"] is None:
            print(" empleados sin sueldo")
            return
    
    print("Nombre Empleado", "\tSueldo Base", "\tDescuento Salud", "\tDescuento AFP", "\tTotal Liquido")
    for trabajador in trabajadores:
        descuento_salud=round(trabajador["Sueldo"] * 0.07)
        descuentoafp=round(trabajador["Sueldo"]* 0.12)
        total_liquido=trabajador["Sueldo"]-descuento_salud-descuentoafp
        print(f"{trabajador["Nombre"]}                {trabajador["Sueldo"]}           {descuento_salud}             {descuentoafp}              {total_liquido}")
                

   


def menu():
    while True:
        input("Presione una tecla para continuar...")
        system("cls")
        print("Programa Empresa")
        try:
            op=int(input("1.Asignar Sueldos Aleatorios\n2.Clasificar Sueldos\n3.Ver Estadisticas\n4.Reporte Sueldos\n5.Salir del programa\n"))
        except ValueError:
            print("Ingrese un valor numerico")
            continue
        if op==1:
            Asignar_Sueldos()
        elif op==2:
            Clasificar_Sueldos()
        elif op==3:
            Ver_Estadistica()
        elif op==4:
            Reporte_sueldos()
        elif op==5:
            print("Saliendo del programa")
            print("Desarrollado por Jose Valdes")
            print("Rut 19.977.738-6")
            break
menu()
