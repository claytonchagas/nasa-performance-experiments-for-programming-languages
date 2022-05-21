from __future__ import print_function
import numpy as np
import sys
from numba import njit
from numba import prange
import Benchmark as dectimer
q=int(input('Digite o número que será usado para calcular a dimensão da matriz(tamanho N), ou seja, o tamanho dela: '))
sysargv_fake=['en.py', q]

@dectimer.bench_time(3)
@njit
def serial_copy(A):
    """
        Perform copies of elements in matrix A iteratively
    """
    N = A.shape[0]
    for i in prange(N):
        for j in prange(N):
            A[i, j, 0] = A[i, j, 1]
            A[i, j, 2] = A[i, j, 0]
            A[i, j, 1] = A[i, j, 2]


@dectimer.bench_time(3)
@njit
def vector_copy(A):
    """
        Perform copies of of elements in matrix A with vectorization
    """
    A[:, :, 0] = A[:, :, 1]
    A[:, :, 2] = A[:, :, 0]
    A[:, :, 1] = A[:, :, 2]


if len(sysargv_fake) < 1:
    print('Usage:')
    print('     python ' + sysargv_fake[0] + ' dimension')
    print('Please specify matrix dimensions')
    sys.exit()

dimension = int(sysargv_fake[1])

print("Numba -- Copy of a matrix: ", dimension)

A = np.random.rand(dimension, dimension, 3)
print(A)
serial_copy(A)
print(A)
print('='*100, 'proximo teste:')
A = np.random.randn(dimension, dimension, 3)
print(A)
vector_copy(A)
print(A)
print(' ')
