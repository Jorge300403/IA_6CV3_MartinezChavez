import pandas as pd

# Ruta al archivo bezdekIris.data
archivo = "C:/Users/jorge/OneDrive/Documentos/JORGE/ESCOM/9_SEMESTRE/IA/LABORATORIO/8_DATASETS/iris/bezdekIris.data"

# Nombres de las columnas según el dataset Iris
columnas = ["logitud sepalo en cm", "ancho sepalo en cm", "longitud petalo en cm", "ancho petalo en cm", "clase"]

# Carga el archivo en un DataFrame
df = pd.read_csv(archivo, header=None, names=columnas)

# Imprime 5  filas del DataFrame
print(df.head())
