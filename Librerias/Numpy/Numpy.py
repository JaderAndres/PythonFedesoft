import numpy as np

import sys
print(sys.executable)

# #array de una dimención
#
# a1 = np.array([1, 2, 3])
# print('-- Array de una dimención: --')
# print(a1)
#
# #array de dos dimenciones
#
# a2 = np.array([[1, 2, 3],[4, 5, 6]])
# print('-- Array de dos dimenciones: --')
# print(a2)
#
# #array de tres dimenciones
#
# a3 = np.array([[[1, 2, 3],[4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print('-- Array de tres dimenciones: --')
# print(a3)

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 1, 1], [2, 2, 2]])
print(a + b)
# [[2 3 4]
#  [6 7 8]]
print(a / b)
# [[1.  2.  3. ]
#  [2.  2.5 3. ]]
print(a ** 2)
# [[ 1  4  9]
#  [16 25 36]]
