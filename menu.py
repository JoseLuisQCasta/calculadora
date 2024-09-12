import os
from funciones import *

def menu():
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            ingresar_primer_operando()
        elif opcion == 2:
            ingresar_segundo_operando()
        elif opcion == 3:
            calcular_todas_las_operaciones()
        elif opcion == 4:
            informar_resultados()
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input("Pulse boton para continuar...")
        os.system('clear')

    
    
menu()
