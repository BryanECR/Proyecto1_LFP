from tkinter import filedialog

class LeerArchivos():
    def abrirArchivo():
        file_path = filedialog.askopenfilename(initialdir = "", title = "Abrir Archivo", filetypes = (("text files", "*.txt"),("all files", "*.*")) )
        archivo = open(file_path, 'r')
        c = archivo.readlines()
        archivo.close()
        print("\n*************************  Cargado con exito  *************************\n")

        return c

