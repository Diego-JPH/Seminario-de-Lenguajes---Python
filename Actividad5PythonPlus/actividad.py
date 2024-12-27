import csv

file_route = "lagos_arg.csv"
#Imprime las 3 provincias con mayores profundidaes maximas entre todos los lagos
def print_report(title, *args):
    print(f"{title.capitalize():-^40}")
    for elem in args:
        print(f"{elem[0]}: {elem[1]}")
        
with open(file_route, "r") as data_set:
    reader = csv.reader(data_set)
    header, data = next(reader), list(reader)
    
my_data = {}

#Almacena en un diccionario la suma de profundidades maximas de todos 
#los lagos en cada provincia  

for row in data:
    num = int(row[3]) if row[3]!="" else 0
    if row[1] in my_data:
        my_data[row[1]] += num
    else:
        my_data[row[1]] = num
        
#Retorna una lista de tuplas de las primeras 5 provincias que contienen
#una mayor profundidad total entre todos los lagos, de mayor a menor
top_ranking = sorted(my_data.items(), key=lambda x: x[1], reverse=True)[:5]
print_report("Super listado", top_ranking[0], top_ranking[1], top_ranking[2])




