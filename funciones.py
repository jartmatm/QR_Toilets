import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog

root = tk.Tk()
root.withdraw()

def Apply_Shift(time):
    if 6 <= time < 14:
        return 'Morning'
    elif 14 <= time < 22:
        return 'Afternoon'
    else:
        return 'Night'  


def load_file():
    """"
    loading data function
    """
    path_file = filedialog.askopenfilename(
        title="Selecciona el archivo Excel",
        filetypes=[("Archivos Excel", "*.xlsx *.xls")]
    )
    if path_file:  # Solo si se seleccionó un archivo
        df = pd.read_excel(path_file)
        print("Archivo cargado exitosamente.")
        return df  
    else:
        print("No se seleccionó ningún archivo.")

def save_file(df):
    """
    saving data function
    """
    path_file = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Archivo Excel", "*.xlsx")],
        title="Guardar archivo como"
    )
    df.to_excel(path_file, index=False)

def save_multiple_sheets(df_dict):
    """
    Guarda múltiples DataFrames en un solo archivo Excel,
    cada uno en una hoja distinta.
    df_dict: diccionario {nombre_hoja: DataFrame}
    """
    path_file = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Archivo Excel", "*.xlsx")],
        title="Guardar archivo como"
    )

    if path_file:  # Si el usuario no canceló
        with pd.ExcelWriter(path_file, engine="xlsxwriter") as writer:
            for sheet_name, df in df_dict.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"Archivo guardado en: {path_file}")

def input_date():
        
    fecha_inicio_str = simpledialog.askstring(
        "Fecha de inicio", "Introduce la fecha de inicio (dd/mm/yyyy HH:MM:SS):")
    fecha_fin_str = simpledialog.askstring(
        "Fecha de fin", "Introduce la fecha de fin (dd/mm/yyyy HH:MM:SS):")

    
    INICIO = pd.to_datetime(fecha_inicio_str, format='%d/%m/%Y %H:%M:%S')
    FIN = pd.to_datetime(fecha_fin_str, format='%d/%m/%Y %H:%M:%S')
    return INICIO, FIN
    

