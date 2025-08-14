import pandas as pd
from variables import (COLUMNAS_ELIMINAR_GRAFITTI, COLUMNAS_RENAME_GRAFITTI, 
                       COLUMNS_TO_CAPITALIZE_GRAFITTI)
from funciones import (load_file, save_file, Apply_Shift, input_date)

df = load_file()
df = df.drop(COLUMNAS_ELIMINAR_GRAFITTI, axis=1)
df = df.rename(columns=COLUMNAS_RENAME_GRAFITTI)
df['Start time'] = pd.to_datetime(df['Start time'], format='%d/%m/%Y %H:%M:%S') 
df['Completion time'] = pd.to_datetime(df['Completion time'], format='%d/%m/%Y %H:%M:%S') 
df['Shift'] = df['Start time'].dt.hour.apply(Apply_Shift)
df['Reporter Name'] = df['Reporter Name'].str.split().str[0]
df['Status'] = df['Status'].str.split('-').str[-1]
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
df.columns = df.columns.str.strip()



for col in COLUMNS_TO_CAPITALIZE_GRAFITTI:
    df[col] = df[col].str.capitalize()

INICIO, FIN = input_date()
df = df[(df['Start time'] >= INICIO) & (df['Start time'] <= FIN)]


save_file(df)
