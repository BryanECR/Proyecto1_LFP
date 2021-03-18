from typing import List

from Lista.Lista import ListaCircular

class Factura:
    def __init__(self) -> None:
        pass    
        
    def datos(arreglo):
        ListaC = ListaCircular()
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
        total = 0
        errores = []
        linea1 = arreglo[0].split(",")

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

            datos = arreglo[contador].split(",")
            
            try:
                cantidad = datos[0]
                int(cantidad)
            except:
                #AGREGARLO COMO ERROR
                cantidad = "cantidad incorrecta"
                informacion = {"Linea":contador,"Error":"Cantidad incorrecta"}
                errores.append(informacion)
            
            #BUSCAR PRODUCTO Y SI NO EXISTE EN LA LISTA AGREGARLO COMO ERROR
            nombreProducto = str(datos[1])
            precio =  ListaC.buscar(str(datos[1])) 

            try:
                precio = float(precio)
            except:
                print("No se pudo convertir el precio")

            if precio == "No existe" or precio == "No hay elementos en la lista":
                informacion = {"Linea":contador,"Error":precio}
                errores.append(informacion)
            else:#REVISAR ESTA PARTE
               html += '<td>\n<td class="tg-3ib7">'+str(cantidad)+'</td>\n<td class="tg-3ib7">'+str(nombreProducto)+'</td>\n<td class="tg-r5us">Q '+str(precio)+'</td>\n<td class="tg-r5us">Q '+str(cantidad*precio )+'</td>\n</tr>'
               SUBtotal += (cantidad*precio)

            contador +=1 

        prop = SUBtotal*propina
        html += '<tr>\n<td class="tg-3ib7" colspan="3">SubTotal</td>\n<td class="tg-r5us">Q '+str(SUBtotal)+'</td>\n</tr>'
        html += '<tr>\n<td class="tg-3ib7" colspan="3">Propina</td>\n<td class="tg-r5us">Q '+str(prop)+'</td>\n</tr>'
        html += '<tr>\n<td class="tg-r5us" colspan="3">Total</td>\n<td class="tg-r5us">Q '+str(SUBtotal+prop)+'</td>\n</tr>'
        html += '</tbody>\n</table>\n</div>\n</body>\n</html>'

        if errores > 1:
            print("El archivo de la factura contiene errores por lo que no fue posible generarlo")
        else:
            file = open("Factura.html","w")
            file.write(html)
            file.close()


