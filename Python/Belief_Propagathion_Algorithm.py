#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import sys
import Benchmark as dectimer
b=["Belief_Propagathion",1000]

@dectimer.bench_time(3)
def belief_propagation(N):
    """
        Run the belief propagation algorithm N times
    """
    dim = 5000
    A = np.random.rand(dim, dim)
    x = np.ones((dim))

    for i in range(N):
        x = np.log(np.dot(A, np.exp(x)))
        x -= np.log(np.sum(np.exp(x)))
    return x

if b[1] < 1:
    print('Usage:')
    print('     python ' + b[0] + ' N')
    print('Please specify the number of iterations.')
    sys.exit()
N = int(b[1])
print('Belief calculations:', N)
y = belief_propagation(N)




