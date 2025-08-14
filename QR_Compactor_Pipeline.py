import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.platypus import SimpleDocTemplate, Image, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from funciones import load_file
from variables import COLUMNAS_ELIMINAR_COMPACTOR, COLUMNAS_RENAME_COMPACTOR

df = load_file()
df["Start time"] = pd.to_datetime(df["Start time"])
df["Completion time"] = pd.to_datetime(df["Completion time"])
df = df.drop(COLUMNAS_ELIMINAR_COMPACTOR, axis=1)
df['Day name'] = df['Start time'].dt.day_name()
df = df.rename(columns=COLUMNAS_RENAME_COMPACTOR)
df['Reporter Name'] = df['Reporter Name'].str.split().str[0]

df_compactor = df[df["What is the origin of the rubbish?"].str.contains(" Waste Porterage", case=False, na=False)]

reportes_por_semana = df_compactor.groupby(pd.Grouper(key="Start time", freq="W")).size()
promedio_semanal = round(reportes_por_semana.mean())

imagenes = []

plt.figure(figsize=(8,5))
sns.countplot(x="Day name", data=df_compactor, color="mediumblue",
              order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
plt.title("Quantity of reports by day")
plt.xlabel("Day of the Week")
plt.ylabel("Quantity of reports for Waste Porterage")
graf1 = "graf_dias.png"
plt.savefig(graf1, bbox_inches="tight", dpi=300)
imagenes.append(graf1)
plt.close()


df_compactor["hour"] = df_compactor["Start time"].dt.hour
plt.figure(figsize=(8,5))
sns.countplot(x="hour", data=df_compactor, color="aqua")
plt.title("Frequency of Waste Porterage by Hour")
plt.xlabel("Hour")
plt.ylabel("Quantity of Reports for Waste Porterage")
graf2 = "graf_horas.png"
plt.savefig(graf2, bbox_inches="tight", dpi=300)
imagenes.append(graf2)
plt.close()

plt.figure(figsize=(10,5))
sns.countplot(y="Reporter Name", data=df_compactor, color="mediumblue",
              order=df_compactor["Reporter Name"].value_counts().index)
plt.title("Waste Porterage reports by cleaner name")
plt.xlabel("Quantity")
plt.ylabel("Cleaner Name")
graf3 = "graf_trabajadores.png"
plt.savefig(graf3, bbox_inches="tight", dpi=300)
imagenes.append(graf3)
plt.close()

fig, ax = plt.subplots(figsize=(6, 3))
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')
ax.axis('off')
ax.text(0.5, 0.6, f"{promedio_semanal}", fontsize=50, fontweight='bold', color='#1300A6', ha='center')
ax.text(0.5, 0.3, "Waste Porterage reports by week", fontsize=12, ha='center')
kpi_img = "kpi_card.png"
plt.savefig(kpi_img, bbox_inches="tight", dpi=300)
imagenes.append(kpi_img)
plt.close()

pdf_filename = "Reporte_Waste_Porterage.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=A4)

elements = []
for img in imagenes:
    elements.append(Image(img, width=15*cm, height=10*cm))
    elements.append(Spacer(1, 1*cm))

doc.build(elements)


print(f"PDF generado: {pdf_filename}")
