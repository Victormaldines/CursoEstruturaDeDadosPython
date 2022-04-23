'''
RECURSÃO 02
SOMAR VALORES
'''

# Loop For
def soma1(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return soma

print(soma1(5))

# Recursão
def soma2(n):
    if n == 0:
        return 0
    return n + soma2(n - 1)

soma2(5)
