import pandas as pd
from funciones import (load_file, input_date, Apply_Shift, save_multiple_sheets)
from variables import (COLUMNAS_ELIMINAR_TOILETS, COLUMNAS_RENAME_TOILETS)

df_collins = load_file()
df_luggage = load_file()
df_BIF = load_file()

for df in [df_collins, df_luggage, df_BIF]:
    df.drop(columns=COLUMNAS_ELIMINAR_TOILETS, errors='ignore', inplace=True)
    df.rename(columns=COLUMNAS_RENAME_TOILETS, inplace=True)
    df['Cleaner name'] = df['Cleaner name'].str.split().str[0]
    df['Start time'] = pd.to_datetime(df['Start time'], format="%m/%d/%Y %I:%M:%S %p")
    df['Completion time'] = pd.to_datetime(df['Completion time'], format="%m/%d/%Y %I:%M:%S %p")
    df['Shift'] = df['Start time'].dt.hour.apply(Apply_Shift)

INICIO, FIN = input_date()
df = df[(df['Start time'] >= INICIO) & (df['Start time'] <= FIN)]

df_collins, df_luggage, df_BIF = [
df[(df['Start time'] >= INICIO) & (df['Start time'] <= FIN)]
    for df in [df_collins, df_luggage, df_BIF]
]

save_multiple_sheets({
    "Collins": df_collins,
    "Luggage": df_luggage,
    "BIF": df_BIF
})

