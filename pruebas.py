def analizarId(cadena):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","w","x","y","z","v","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","_"]
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    cadena1 = str(cadena).strip()
    caracteres = list(cadena1)

    for i in range(len(caracteres)):
            
        if caracteres[i] in letras or caracteres[i] in numeros:
            pass
        else:
            print("caracter desconocido: "+str(caracteres[i]))
            

id1 = "asdf"
id2 = "as/dad8"
id3 = "98-7"
id4 = "asd*asd_65"
id5 = "asfds233_5"


analizarId(id1)
analizarId(id2)
analizarId(id3)
analizarId(id4)
analizarId(id5)