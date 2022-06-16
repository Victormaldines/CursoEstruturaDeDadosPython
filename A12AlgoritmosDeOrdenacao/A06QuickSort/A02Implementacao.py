import numpy as np

def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1

    for j in range(inicio, final):
      if vetor[j] <= pivo:
        i += 1
        vetor[i], vetor[j] = vetor[j], vetor[i] # swap
    vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
    return i + 1

def quick_sort(vetor, inicio, final):
    if inicio < final:
      posicao = particao(vetor, inicio, final)
      # esquerda
      quick_sort(vetor, inicio, posicao - 1)
      # direita
      quick_sort(vetor, posicao + 1, final)
    return vetor

vetor = np.array([15, 34, 8, 3])
quick_sort(vetor, 0, len(vetor) - 1)

print(vetor)

vetor1 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
quick_sort(vetor1, 0, len(vetor1) - 1)

print(vetor1)
