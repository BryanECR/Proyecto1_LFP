from Lectura import LeerArchivos
from Lista import ListaCircular
from Analizar import Analizar

class Menu:

    def menu():
        LineasMenu = ""
        lineasOrden = ""
        while(True):
            datosMios = '''
                ********* Proyecto 1 *********
                Nombre: Bryan Eduardo Caal Racanac
                Carnet: 201801155
                Curso: Lenguajes Formales de Programacion
                Seccion: B-
            '''
            menu = '''  
            ***********************     MENU    ***********************
            *                   1. Cargar Menu                        *
            *                   2. Cargar Orden                       *
            *                   3. Generar Menu                       *
            *                   4. Generar Factura                    *
            *                   5. Generar Arbol                      *
            *                   6. Salir                              *
            ***********************************************************
            '''
            print(datosMios)
            print(menu)
            Opcion = int(input("Ingrese la opcion que desee ejecutar: "))
            if(Opcion == 1):
                LineasMenu = LeerArchivos.abrirArchivo()

                print(LineasMenu)

            elif(Opcion == 2):
                lineasOrden = LeerArchivos.abrirArchivo()
                print(lineasOrden)
            elif(Opcion == 3):
                listaC = ListaCircular()
                if listaC.verificar() == "No hay elementos en la lista":
                    print("Error: No se ah cargado ningun menu con anterioridad ")
                else:
                    print("\n*************************** Menu Generado con exito ***************************")
            elif(Opcion == 4):
                listaC = ListaCircular()
                if listaC.verificar() == "No hay elementos en la lista":
                    print("Error: No se ah cargado ningun menu con anterioridad ")
                else:
                    print("\n*************************** Factura Generada con exito ***************************")
            elif(Opcion == 5):
                print("OPCION VALIDA")
            elif(Opcion == 6):
                print("\n¡Hasta la proxima!\n")
                break
            else:
                print("\n*********** !Opcion Invalida¡ ***********\nIngrese por teclado numerico la opcion que desea ejecutar\n")

Menu.menu()