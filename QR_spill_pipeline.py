import pandas as pd
from funciones import (load_file, Apply_Shift, save_file, input_date)
from variables import (COLUMNAS_RENAME_SPILL, COLUMNS_TO_CAPITALIZE_SPILL)

df = load_file()
df = df.drop(['Name', 'Email'], axis=1)
df = df.rename(columns=COLUMNAS_RENAME_SPILL)

df['Start time'] = pd.to_datetime(df['Start time'], format='%d/%m/%Y %H:%M:%S') 
df['Completion time'] = pd.to_datetime(df['Completion time'], format='%d/%m/%Y %H:%M:%S')

df['Shift'] = df['Start time'].dt.hour.apply(Apply_Shift)

df['Reporter Name'] = df['Reporter Name'].str.split().str[0] #eliminar el apellido del que reporta
df['Status'] = df['Description'].str.split('-').str[-1] # crea la columna estatus apartir de descripcion con la segunda parte
df['Description'] = df['Description'].str.split('-').str[0] # elimina la segunda parte de la columna descripcion
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col) #elimina los espacios al principio y al final de todos los datos
df.columns = df.columns.str.strip() # eliminar espacios al inicio y al final de las columnas


for col in COLUMNS_TO_CAPITALIZE_SPILL:
    df[col] = df[col].str.capitalize()

INICIO, FIN = input_date()
df = df[(df['Start time'] >= INICIO) & (df['Start time'] <= FIN)]

save_file(df)
