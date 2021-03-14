cadena1 = "         '    Bebidas Alcoholicas':"
cadena2 = "'    Descripción Bebida 1'"
cadena3 = "'Bebida #1'"
id1 = "bebidaA_1"
id2 = "d1 ?"
precio1 = " 45. 00 "
precio2 = "40 ."
precio3 = "35   .A"

class Analizador:
    def analizarID(cadena):
        print("id")

    def analizarPrecio(cadena):
        numero = str(cadena).replace(" ","")
        try:
            numero = float(numero)
            return "Exito"
        except:
            return "Error"

    def analizarCadenas(cadena):
        cadena2 = str(cadena).replace("'","")
        cadena2 = cadena2.strip()
        cadena2 = cadena2.replace(":","")
        print(cadena2)

    
cadena1 = "'Bebidas' Alcoholicas': &&&&"
cadena1 = list(cadena1)
print(cadena1)

contador = 0
for i in range(len(cadena1)):
    if cadena1[i] == "'":
        contador += 1

print(contador)