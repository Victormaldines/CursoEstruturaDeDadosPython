'''
SELECTION SORT
Debug
'''

import numpy as np
def selection_sort(vetor):
    n = len(vetor)

    for i in range(n-1):
        index_minimo = i

        for j in range(i + 1, n):
            if vetor[index_minimo] > vetor[j]:
                index_minimo = j

        temp = vetor[i]
        vetor[i] = vetor[index_minimo]
        vetor[index_minimo] = temp

vetor = np.array([15, 34, 8, 3])
selection_sort(vetor)
