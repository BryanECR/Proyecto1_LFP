from Funciones.Lectura import LeerArchivos

def analizarOrden():
    print("Analizar Menu")

def analizarMenu():
    print("Analizar Menu")


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
        elif(Opcion == 3):
            print("OPCION VALIDA")
        elif(Opcion == 4):
            print("OPCION VALIDA")
        elif(Opcion == 5):
            print("OPCION VALIDA")
        elif(Opcion == 6):
            print("\n¡Hasta la proxima!\n")
            break
        else:
            print("\n*********** !Opcion Invalida¡ ***********\nIngrese por teclado numerico la opcion que desea ejecutar\n")
        

menu()