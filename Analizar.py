import os
from Lista.Lista import ListaCircular

ListaC = ListaCircular()
class Analizar:
    
    
    def analizarPrecio(cadena):
        numero = str(cadena).replace(" ","")
        try:
            numero = float(numero)
            return '{:.2f}'.format(numero)
        except:
            return "No es un numero"

    def analizarCadenas(cadena,linea):

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
             

        #SI LA ESTRUCTURA DE LA CADENA ES CORRECTA SE PROCEDE A GENERAR LA CADENA
        else:

            empieza = int(rango[0]+1)
            termina = int(rango[1])
            cadena = ""
            while(empieza < termina):
                cadena += caracteres[empieza]
                empieza += 1

            #Toma como error los caracteres fuera de las comillas
            if termina < len(caracteres):
                contador = termina+1
                
                while(contador < len(caracteres)):

                    if caracteres[contador] != "\n" or caracteres[contador] != " ":
                       # -- print("caracter Desconocido: "+str(caracteres[contador]))
                       errores = {"Linea": linea, "Error":"Caracter Desconocido "+str(caracteres[contador])}

                    contador += 1

            cadena = str(cadena).strip()

            return cadena

    def anadlizarID(cadena):
        letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","w","x","y","z","v","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","_"]
        numeros = ["0","1","2","3","4","5","6","7","8","9"]
        cadena1 = str(cadena).strip()
        caracteres = list(cadena1)
        id = ""

        for i in range(len(caracteres)):
            
            if caracteres[i] in letras or caracteres[i] in numeros:
                id += str(caracteres[i])
            else:
                return "Id no valido"

        return id
            
    
    def analizarMenu(arreglo):
        global ListaC
        html = '''<html lang="es">
         <head>
            <meta charset="Utf-8">
            <title>Menu</title>
            <style>
            *{
                margin: 0px;
                padding: 0px;
            }
            body{
                background: url("8Vn79j.jpg");
                background-attachment: fixed;
            }
            .content{
                background-color: azure;
                margin: 30%;
                padding: 5%;
            }
            .titulo{
                font-family:'Times New Roman', Times, serif;
                text-align: center;
            }
            .categoria {
                font-family: 'Courier New', Courier, monospace;
            }
            .producto{
                display: inline;
            }
            </style>
        </head>
        <body background="8Vn79j.jpg">
        <div class="Content">'''

        errores = []
        grafica = ""
        NumeroCategoria = 0
        NumeroHijo = 0
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
                    if nombre[contador] != " " or nombre[contador] != "\n" :
                        informacion = {"Linea":1,"Error":"Caracter desconocido fuera de la cadena"}
                        errores.append(informacion)
                    contador +=1

        # -- print("Nombre: "+str(nombreR))
        html += '<h1 class="titulo" >'+str(nombreR)+'</h1>'
        grafica += 'A[label="'+str(nombreR)+'"]\n'
        #ANALIZAR EL RESTO DEL ARCHIVO
        contador = 1
        while(contador < len(arreglo)):
            caracteres = str(arreglo[contador]).strip()
            caracteres = list(arreglo[contador])
            
            
        # 1. SI EMPIEZA CON ' ES UNA CATEGORIA
            if caracteres[0] == "'":
                categoria = Analizar.analizarCadenas(arreglo[contador],contador)
                
                if categoria == "Comillas de mas en la cadena" or categoria == "Faltan comillas" or categoria == "Caracteres de mas fuera de la cadena":

                    informacion = {"Linea": contador,"Error": categoria}
                    errores.append(informacion)

                else:
                    
                    # -- print("\nCategoria: "+str(categoria))
                    html += '<h2 class="categoria">'+str(categoria)+'</h2>'
                    grafica += 'Categoria'+str(NumeroCategoria)+'[label = "'+categoria+'"]\n'
                    grafica += "A -> "+'Categoria'+str(NumeroCategoria)+"\n"
                    NumeroCategoria += 1

        # 2. SI EMPIEZA COM [ ES UN PRODUCTO
            elif caracteres[0] == "[":
                cadena = str(arreglo[contador]).strip().replace("[","").replace("]","")
                secciones = str(cadena).split(";")
                id = Analizar.anadlizarID(secciones[0]) 
                Nombre = Analizar.analizarCadenas(secciones[1],contador) 
                Precio = Analizar.analizarPrecio(secciones[2]) 
                Descripcion = Analizar.analizarCadenas(secciones[3],contador) 

                if id == "Id no valido":
                    informacion = {"Linea":contador,"Error":id}
                    errores.append(informacion)
                elif Nombre == "Comillas de mas en la cadena" or Nombre == "Faltan comillas":
                    informacion = {"Linea":contador,"Error":Nombre}
                    errores.append(informacion)
                elif Precio == "No es un numero":
                    informacion = {"Linea":contador,"Error":Precio}
                    errores.append(informacion)
                elif Descripcion == "Comillas de mas en la cadena" or Descripcion == "Faltan comillas":
                    informacion = {"Linea":contador,"Error":Descripcion}
                    errores.append(informacion)
                else:
                    ListaC.incertar(id,Nombre,Precio)
                    html += '<h3 class="producto">&emsp;'+str(Nombre)+'</h3><h3 class="producto">&emsp;Q '+str(Precio)+'</h3>'
                    html += '<p>&emsp;'+str(Descripcion)+'</p>'
                    grafica += 'CategoriaHijo'+str(NumeroHijo)+'[label = "'+str(Nombre)+" "+str(Precio)+ '"]\n'
                    grafica += 'Categoria'+str(NumeroCategoria-1)+" -> "+'CategoriaHijo'+str(NumeroHijo)+"\n"
                    NumeroHijo += 1

        # 3. CUALQUIER LINEA DIFERENTE SERA UN CARACTER DESCONOCIDO
            elif caracteres[0] != "\n":
                informacion = {"Linea": contador,"Error":"Caracter Desconocido: "+str(arreglo[contador])}
                errores.append(informacion)

        
            contador += 1
            
        html += "   </div>\n   </body>\n</html>"
        
        if len(errores) > 1:
            print("El Documento tiene errores por lo que no es porsible generar el Menu")
            htmlerrores = '''
            <html lang="es">
                <head>
                    <meta charset="utf-8">
                    <title>Errores</title>
                    <style>
                        table, th, td {
                            border: 1px solid black;
                        }
                    </style>
                </head>
                <body>
                <div class="content">
                    <h1 align = "center">TABLA DE ERRORES</h1>
                    <table class="default" align = "center">
                        <tr>
                         <th>Numero</th>
                         <th>Linea</th>
                         <th>Error</th>
                        </tr>
                '''
                
            for i in range(len(errores)):
                htmlerrores += "<tr>\n<td>"+str(i+1)+"</td>\n"
                htmlerrores += "<td>"+str(errores[i]['Linea'])+"</td>\n"
                htmlerrores += "<td>"+str(errores[i]['Error'])+"</td>\n</tr>"

            htmlerrores += "</table>\n</div>\n</body>\n</html>"
            file = open("Errores.html","w")
            file.write(htmlerrores)
            file.close()
        else:
            #GENERA EL HTML SI EL ARCHIVO NO TIENE ERRORES
            file = open("Menu.html","w")
            file.write(html)
            file.close()
            #GENERA LA GRAFICA PARA EL ARCHIVO
            file = open("Grafica.dot","w")
            file.write("digraph G {\n"+str(grafica)+"\n}")
            file.close()
            os.system('dot -Tpng Grafica.dot -o Grafica.png')
            
 #*****************************************************************************************************    
    def ver():
        return ListaC.recorrer()
   
        
    def datos(arreglo):
        html = '''
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title>Factura</title>
        <style type="text/css">
            .tg  {border-collapse:collapse;border-spacing:0;}
            .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
              overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
              font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg .tg-9gth{border-color:inherit;font-family:"Courier New", Courier, monospace !important;;text-align:left;vertical-align:top}
            .tg .tg-3ib7{border-color:inherit;font-family:"Courier New", Courier, monospace !important;;text-align:center;vertical-align:top}
            .tg .tg-r5us{font-family:"Courier New", Courier, monospace !important;;text-align:center;vertical-align:top}
            </style>
        </head>
        <body>
        <div class="content"> '''
        
        errores = []
        linea1 = arreglo[0].split(",")

        print(linea1)

        nombre = str(linea1[0]).strip().replace("'","")
        nit = str(linea1[1]).strip().replace("'","")
        direccion = str(linea1[2]).strip().replace("'","")
        propina =  str(linea1[3]).replace("%","").strip()
        try:
            propina = float(propina)
        except:
            informacion = {"Linea":1,"Error":"Valor de la propina incorrecto: "+str(propina)}

        html += "<h1>Datos del cliente</h1>\n<h2>Nombre: "+str(nombre)+"</h2>\n<h2>NIT: "+str(nit)+"</h2>\n<h2>Dirección: "+str(direccion)+"</h2>\n"

        html += '''  <table class="tg" align = "center">
                <thead>
                  <tr>
                    <th class="tg-9gth" colspan="4">Descripción del Consumo</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="tg-3ib7">Cantidad</td>
                    <td class="tg-3ib7">Concepto</td>
                    <td class="tg-r5us">Precio</td>
                    <td class="tg-r5us">Total</td>
                  </tr>'''


        #-- datosCliente = {'Nombre':nombre,'Nit':nit,'Direccion':direccion,'Propina':propina}
        # -- print(datosCliente)

        lineas = len(arreglo)
        contador  = 1
        SUBtotal  = 0
        
        while(contador < lineas):

            datos = str(arreglo[contador]).strip().split(",")
            
            try:
                cantidad = datos[0]
                cantidad = int(cantidad)
            except:
                #AGREGARLO COMO ERROR
                cantidad = "cantidad incorrecta"
                informacion = {"Linea":contador,"Error":"Cantidad incorrecta"}
                errores.append(informacion)
            
            #BUSCAR PRODUCTO Y SI NO EXISTE EN LA LISTA AGREGARLO COMO ERROR
            nombreProducto = str(datos[1])
            precio =  ListaC.buscar(nombreProducto) 
            print(datos[0],datos[1],precio)

            
            try:
                precio = float(precio)
            except:
                print("")
                

            if precio == "No existe" or precio == "No hay elementos en la lista":
                informacion = {"Linea":contador,"Error":precio}
                errores.append(informacion)
            else:#REVISAR ESTA PARTE
               html += '<tr>\n<td class="tg-3ib7">'+str(cantidad)+'</td>\n<td class="tg-3ib7">'+str(nombreProducto)+'</td>\n<td class="tg-r5us">Q '+str(precio)+'</td>\n<td class="tg-r5us">Q '+str(cantidad*precio )+'</td>\n</tr>'
               SUBtotal += (cantidad*precio)

            contador +=1 

        prop = SUBtotal*(propina/100)
        html += '<tr>\n<td class="tg-3ib7" colspan="3">SubTotal</td>\n<td class="tg-r5us">Q '+str(SUBtotal)+'</td>\n</tr>'
        html += '<tr>\n<td class="tg-3ib7" colspan="3">Propina</td>\n<td class="tg-r5us">Q '+str(prop)+'</td>\n</tr>'
        html += '<tr>\n<td class="tg-r5us" colspan="3">Total</td>\n<td class="tg-r5us">Q '+str(SUBtotal+prop)+'</td>\n</tr>'
        html += '</tbody>\n</table>\n</div>\n</body>\n</html>'

        if len(errores) > 1:
            print("El archivo de la factura contiene errores por lo que no fue posible generarlo")
        else:
            file = open("Factura.html","w")
            file.write(html)
            file.close()
        

# 1. BUSCAR EL NOMBRE DEL ID QUE SE BUSCA PARA GENERAR LA FACTURA