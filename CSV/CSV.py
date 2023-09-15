
# Lectura

import csv

with open('PruebaCSV.csv', newline='') as archivo:
    lineas = csv.reader(archivo)
    for i, linea in enumerate(lineas, 1):
        print(', '.join(linea))
        # if i >= 5:
        #     break
print('-'*70)