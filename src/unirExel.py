from tkinter import filedialog
import pandas as pd
import os
import re
import openpyxl

def main():
     leer = leer_archivos()

def leer_archivos(): 
    directory = filedialog.askdirectory()
    os.chdir(directory)
    files=[x for x in os.listdir() if re.search('.csv$',x)]
    print(files)
    ordenarExcel=[]
    df=pd.DataFrame()

    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".csv")
    rutaArchivo = os.path.basename(nombre_archivo)
   
    for f in files:
        archivo=pd.read_excel(f,engine='openpyxl')
        ordenarExcel.append(archivo)
        df=pd.concat(ordenarExcel)
        
        with pd.ExcelWriter(rutaArchivo) as writer:
            df.to_excel(writer,rutaArchivo,index=False)

if __name__ == '__main__':
    main()      