a = ["'Erick Samuel','6655443-6','Ciudad',1.5%\n", '2,crun-chy\n', '1,b5capas\n', '2,stacker\n', '3,gordita ?\n', '1,crunchy\n', '2,n_supreme\n', '3,bb3\n', '3,bb3\n', '3,b']

class Factura:
    def __init__(self) -> None:
        pass    
        
    def datos(arreglo):
        errores = []

        linea1 = arreglo[0].split(",")

        nombre = str(linea1[0]).strip().replace("'","")
        nit = str(linea1[1]).strip().replace("'","")
        direccion = str(linea1[2]).strip().replace("'","")
        propina =  str(linea1[3]).replace("%","").strip()
        try:
            propina = float(propina)
        except:
            print("Error")

        datosCliente = {'Nombre':nombre,'Nit':nit,'Direccion':direccion,'Propina':propina}
        print(datosCliente)

        lineas = len(arreglo)
        contador  = 1
        SUBtotal  = 0
        cuenta = []
        
        while(contador < lineas):

            datos = arreglo[contador].split(",")
            
            try:
                cantidad = datos[0]
                int(cantidad)
            except:
                #AGREGARLO COMO ERROR
                cantidad = "cantidad incorrecta"
            
            #BUSCAR PRODUCTO Y SI NO EXISTE EN LA LISTA AGREGARLO COMO ERROR
            producto = datos[1].strip()

            
            # 1. SI CANTIDAD ES IFUAL A ERROR NO SUMARLO
            # 2. MULTIPLICAR LA CANTIDAD POR EL PRECIO DEL PRODUCTO
            # 3. MULTIPLICAR EL SUB TOTAL POR LA PROPINA
            # 4. SUMAR EL SUB TOTAL Y LA PROPINA Y AGREGARLO A TOTAL
            SUBtotal += int(cantidad)
            print(cantidad,producto)



            contador +=1 

        print("total de productos: "+str(total))


Factura.datos(a)