# x=0
# def set_x():
#     # global x
#     # x=77
#     print(x)
#
# set_x()
import glob

import chardet

# a, b, c = 1, 2, 3
# def change_values(a, c):
#     global b
#     print(a, b, c)
#     a,b,c = 0,0,0
#
# def main():
#     global a
#     a=-1
#     change_values(c,a)
#     print(a,b,c)
#
# main()

# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num-1)
# print(factorial(0))
# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(5))

# //////////////////////////////////
print("File".ljust(110), "Encoding")
# for filename in glob.glob('C:/ConsolidadoSP_SiesaRelease/procedimientosalmacenados/*.sql'):
for filename in glob.glob('C:/BI-RAD/1. INCIDENTES/23.06.01/Realizar proceso de validación de fuentes de ORACLE para UnoBiable - 279696/VistasFinancieroORACLE/TodasVistasORACLEUnoBiableFinanciero/*.pdc'):
    with open(filename, 'rb') as rawdata:
        result = chardet.detect(rawdata.read())
    print(filename.ljust(110), result['encoding'])
# ///////////////////////////////