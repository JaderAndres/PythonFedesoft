'''
#ARCHIVOS

with open('C:/DiplomadoPython/PythonFedesoft/ArchivosDirectorios/poema.txt', 'w') as f:
    f.write('Amo mucho a Selena Gómez')

with open('C:/DiplomadoPython/PythonFedesoft/ArchivosDirectorios/poema.txt', 'a') as f:
    f.write('Selena Gómez es mi amor')

archivo = open(
    'C:/DiplomadoPython/PythonFedesoft/ArchivosDirectorios/poema.txt', 'r')
for linea in archivo:
    print(linea, end='')
archivo.close()
'''

# MODULO OS - ARCHIVOS

import os

# LISTDIR
# dir_cont = os.listdir(r"C:/DiplomadoPython/PythonFedesoft/ArchivosDirectorios")
# for archivo in dir_cont:
#    print(archivo)

# RENAMES

postres = 'C:/DiplomadoPython/PythonFedesoft/ArchivosDirectorios/Postres.txt'
comida = 'C:/DiplomadoPython/PythonFedesoft/ArchivosDirectorios/Comidas.txt'


def postres2comida():
    os.renames(postres, comida)
    print('Renombrado:', postres, 'to', comida)


def comida2postres():
    os.renames(comida, postres)
    print('Renombrado', comida, 'to', postres)


def main():
    postres2comida()


if __name__ == "__main__":
    main()
