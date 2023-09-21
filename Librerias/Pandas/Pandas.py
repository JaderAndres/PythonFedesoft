import pandas as pd

""" df = pd.read_csv("C:/DiplomadoPython/PythonFedesoft/Librerias/Pandas/kaggle-titanic-master/data/test.csv")
print(df) """

# DataFrame a partir de un Diccionario

""" unidades_2015 = {"Ag": 2, "Au": 5, "Cu": 3, "Pt": 2}
unidades_2016 = {"Ag": 4, "Au": 6, "Cu": 7, "Pt": 2}
unidades_2017 = {"Ag": 3, "Au": 2, "Cu": 4, "Pt": 1}
unidades = pd.DataFrame([unidades_2015, unidades_2016,
                        unidades_2017], index=[2015, 2016, 2017])
print(unidades) """

# Importar datos desde un fichero de texto plano

""" df = pd.read_csv("con.txt", sep = " ")
print(df) """

# Exportar datos desde un DataFrame hacia archivos CSV y tipo Excel

# CSV
# 1. Primero leer CSV:
df = pd.read_csv(
    "C:/DiplomadoPython/PythonFedesoft/Librerias/Pandas/kaggle-titanic-master/data/train.csv")
print(df)
# 2. Exportar a CSV:
df.to_csv("train_exportado.csv")

# EXCEL
# 1. Primero leer CSV:
df = pd.read_excel(
    "C:/DiplomadoPython/PythonFedesoft/Librerias/Pandas/kaggle-titanic-master/data/train.xlsx")
print(df)
# 2. Exportar a Excel:
df.to_excel("train_exportado.xlsx")
