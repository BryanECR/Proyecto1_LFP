

class Analizar:

    def analizarPrecio(cadena):
        numero = str(cadena).replace(" ","")
        try:
            numero = float(numero)
            return '{:.2f}'.format(numero)
        except:
            return "No es un numero"

    def analizarCadenas(cadena):
        cadena1 = str(cadena)
        cadena1 = cadena1.strip()
        cadena1 = cadena1.replace(":","")
        cadena1 = cadena1.strip()
        caracteres = list(cadena1)
        rango = []

        #TOMA LAS POSICIONES DONDE EXISTEN LAS COMILLAS
        for i in range(len(caracteres)):
            if caracteres[i] == "'":
                rango.append(i)

        #SI EXISTEN MAS DE DOS COMILLAS ES UN ERROR
        if len(rango) > 2:
            
            return "Comillas de mas en la cadena"

        elif len(rango) == 1:

            return "Faltan comillas"
             

        #SI EL EXISTEN MAS CARACTERES DESPUES DE LA ULTIMA COMILLA EXISTE UN ERROR
        elif rango[1] < len(caracteres)-1:

            return "Caracteres de mas fuera de la cadena"

        #SI LA ESTRUCTURA DE LA CADENA ES CORRECTA SE PROCEDE A GENERAR LA CADENA
        else:

            empieza = int(rango[0]+1)
            termina = int(rango[1])
            cadena = ""
            while(empieza < termina):
                cadena += caracteres[empieza]
                empieza += 1

            cadena = str(cadena).strip()
            return cadena


    def analizarOrden(arreglo):
        errores = []
        datos = []
        nombreR = ""
        letras = ['r','e','s','t','a','u','r','a','n','t','e','R','E','S','T','A','U','R','A','N','T','E','=',"'"," "]
        #ANALIZAR LA PRIMERA LINEA
        nombre = arreglo[0].strip()
        nombre = list(nombre)
        cantidadDeIguales = []
        cantidadDeComilals = []
        primeraComilla = nombre.index("'")
        contador = 0
        #SI RESTAURANTE ESTA BIEN ESCRITO
        while(contador < primeraComilla):
            if nombre[contador] in letras:
                contador +=1
                continue
            else:
                informacion = {"Linea":1,"Error":"Error lexico"}
                errores.append(informacion)
            contador +=1

        for i in range(len(nombre)):            
            if nombre[i] == "=":
                cantidadDeIguales.append(i)
            elif nombre[i] == "'":
                cantidadDeComilals.append(i)

        # SI EXISTE SOLO UN IGUAL
        if len(cantidadDeIguales) > 1:
            informacion = {"Linea":1,"Error": "Existe mas de un igual"}
            errores.append(informacion)

        
        
        # HACER CADENA DENTRO DE LAS COMILLAS
        if len(cantidadDeComilals) == 1:
            informacion = {"Linea":1,"Error":"Falta una comilla"}
            errores.append(informacion)
        elif len(cantidadDeComilals) > 2:
            informacion = {"Linea": 1,"Error":"Existen mas de dos comillas"}
            errores.append(informacion)
        elif len(cantidadDeComilals) == 2:
            contador = cantidadDeComilals[0] +1
            while(contador < cantidadDeComilals[1]):
                nombreR += nombre[contador]
                contador += 1
            informacion = {"Lexema":nombreR,"Token": "cadena"}
            datos.append(informacion)
            # SI EXISTE UN CARACTER FUERA DE LAS COMILLAS REPORTARLO COMO ERROR
            if cantidadDeComilals[1] < len(nombre):
                contador = cantidadDeComilals[1]
                while(contador < len(nombre)):
                    informacion = {"Linea":1,"Error":"Caracter desconocido fuera de la cadena"}
                    errores.append(informacion)
                    contador +=1

        print("Nombre: "+str(nombreR))
        #ANALIZAR EL RESTO DEL ARCHIVO
        contador = 1
        while(contador < len(arreglo)):
            caracteres = str(arreglo[contador]).strip()
            caracteres = list(arreglo[contador])
            
            
        # 1. SI EMPIEZA CON ' ES UNA CATEGORIA
            if caracteres[0] == "'":
                categoria = Analizar.analizarCadenas(arreglo[contador])
                
                if categoria == "Comillas de mas en la cadena" or categoria == "Faltan comillas" or categoria == "Caracteres de mas fuera de la cadena":

                    informacion = {"Linea": contador,"Error": categoria}
                    errores.append(informacion)

                else:
                    
                    print("\nCategoria: "+str(categoria))

        # 2. SI EMPIEZA COM [ ES UN PRODUCTO
            elif caracteres[0] == "[":
                cadena = str(arreglo[contador]).strip().replace("[","").replace("]","")
                secciones = str(cadena).split(";")
                Nombre = secciones[1]
                Precio = secciones[2]
                Descripcion = secciones[3]

                print("Identificador: "+str(secciones[0]),"Nombre: "+str(secciones[1]),"Precio: "+str(secciones[2]),'Descripcion: '+str(secciones[3]))
            
            elif caracteres[0] != "\n":
                print("caracter Desconocido: "+str(arreglo[contador]))

        
            contador += 1

arreglo = ["restaur$sante=='Restaurante LFP'%", "'Bebidas' :\n", "[bebida_1;'Bebida #1';11.;'Descripción Bebida 1'    ]\n", "[ bebida_2;'Bebida #2';10.50;'Descripción Bebida 2']\n", "[ bebida_3;'Bebida #2';10.50; 'Descripción Bebida 2']\n", "[ bebida_4;'Bebida #2';10.50;'Descripción Bebida 2']\n", "[ bebida_5;'Bebida #2';10.50;    'Descripción Bebida 2']\n", '\n', "'Desayunos':\n", "[d1;'Desayuno 1';45.00;'Descripción']\n", "[d2 ;'Desayuno 2'; 40.   ;'Descripción']\n", "[d3;'Desayuno 3';35;'Descripción']\n", '\n', "'  Postres':\n", "[   pos_001;'Postre 1'   ;25;'Descripción']\n", "[ pos_002;    'Postre 1';25;'Descripción']\n","@", "[ pos_003;'Postre 1'   ;25;'Descripción']\n", "[   pos_004;    'Postre 1';25;'Descripción']\n", "[ pos-004;'Postre 1'   ;  25;'Descripción']"]

Analizar.analizarOrden(arreglo)

# 1. DIVIDIR LA SECCION DE LA CADENA PARA ANALIZARLOS POR SEPARADO
# 2. TOMAR EL ARREGLO DE ERROR COMO ARREGLO GLOBAL
# 3. ARREGLAR EL QUE SI EXISTE UN CARACTER FUERA DE LA CADENA SE REPORTE COMO ERROR
# 3. CREAR EL HTML