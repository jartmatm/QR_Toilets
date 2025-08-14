import pandas as pd
from funciones import (Apply_Shift, load_file, save_file, input_date)
from variables import (COLUMNAS_RENAME_BINS, COLUMNAS_ELIMINAR_BINS, BINS_DICT, COLUMNS_TO_CAPITALIZE_BINS)


df = load_file()
df = df.rename(columns=COLUMNAS_RENAME_BINS) #renombrar columnas

df['Start time'] = pd.to_datetime(df['Start time'], format='%d/%m/%Y %H:%M:%S') #convertir formato datetime
df['Completion time'] = pd.to_datetime(df['Completion time'], format='%d/%m/%Y %H:%M:%S') #convertir formato datetime
df['Shift'] = df['Start time'].dt.hour.apply(Apply_Shift) # funcion para crear columna shift con horarios
df['Reporter Name'] = df['Reporter Name'].str.split().str[0] #eliminar el apellido del que reporta
df['Platform'] = df['Platform'].str.split(' ').str[-1] # elimina la segunda parte de la columna Platform
df.columns = df.columns.str.strip() # eliminar espacios al inicio y al final de las columnas
df['Platform'] = df['Platform'].replace('4/3', '3/4') #cambiar los valores 4/3 de la columna platform a 3/4
df['Please list the bins you emptied'] = df['Please list the bins you emptied'].str.replace(
    'All bins listed;', 
    'All bins listed.;', 
    regex=False
) #cambiar los valores All bins listed sin punto por All bins listed con punto
df['Day name'] = df['Start time'].dt.day_name() #crea una nueva con los nombres de los dias

df['Were bins stations emptied and replaced with a new liner?'] = df[['Were bins stations emptied and replaced with a new liner?',
                                                                      'Were bins stations emptied and replaced with a new liner?temp',
                                                                      'Were bins stations emptied and replaced with a new liner?2',
                                                                      'Were bins stations emptied and replaced with a new liner?3']].fillna('').astype(str).agg(' '.join, axis=1) #une tres columnas
df['Please list the bins you emptied'] = df[['Please list the bins you emptied',
                                             'Please list the bins you emptied2',
                                             'Please list the bins you emptied3',
                                             'Please list the bins you emptied4']].fillna('').astype(str).agg(' '.join, axis=1) #une tres columnas
df = df.drop(COLUMNAS_ELIMINAR_BINS, axis=1) #eliminar columnas que no se utilizan

df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col) #elimina los espacios al principio y al final de todos los datos

col_texto = 'Please list the bins you emptied'

df[col_texto] = df[col_texto].fillna('').astype(str)
df[col_texto] = df[col_texto].apply(lambda x: x if x.endswith(';') else x + ';') #se asegura que el separador sea ;

for col_name, search_text in BINS_DICT.items():
    pattern = f"{search_text};"
    df[col_name] = df[col_texto].apply(
        lambda x: pattern in str(x).replace('\xa0', ' ')
    ).astype(int)  #crea columnas con los valores de las celdas

for col in COLUMNS_TO_CAPITALIZE_BINS:
    df[col] = df[col].str.capitalize() #pone en mayuscula la primera letra de las columnas description y reporter name


df = df.sort_values(by=['Platform', 'Start time'])
df['FechaAnterior'] = df.groupby('Platform')['Start time'].shift(1)
df['TiempoDesdeEventoAnterior'] = (
    df['Start time'] - df['FechaAnterior']
).dt.total_seconds() / 60  #Calcula la diferencia en minutos convierte a minutos

INICIO, FIN = input_date()
df = df[(df['Start time'] >= INICIO) & (df['Start time'] <= FIN)]

save_file(df)

