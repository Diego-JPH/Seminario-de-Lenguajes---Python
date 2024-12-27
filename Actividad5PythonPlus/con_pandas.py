import pandas as pd

file_route = "lagos_arg.csv"
#Imprime las 3 provincias con mayores profundidaes maximas entre todos los lagos
def print_report(title, ranking):
    print(f"{title.capitalize():-^40}")
    print(ranking.head(3))
        
data_set = pd.read_csv(file_route)
prov_max_depth = data_set.groupby('Ubicación')['Profundidad máxima (m)'].sum()
top_ranking = prov_max_depth.sort_values(ascending=False)
print_report("Super listado", top_ranking)

#Un dataframe:
#print(data_set)

#Una serie:
#print(data_set['Nombre'])

#Columnas de un dataset:
#print(data_set.columns)

#Tipos de datos de cada columna:
#print(data_set.dtypes)

#Ventajas de usar Pandas en un archivo csv:
#Manipulacion eficiente de los datos
#Codigo mas facil de leer y escribir
#Filtrado de datos (para valores nulos)
#Brinda facilidades para calculos matematicos
#Permite implementar otras librerias para el grafico de datos