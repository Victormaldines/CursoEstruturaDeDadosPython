'''
1. O fatorial de um número inteiro m não negativo, é indicado por m! (lê-se "m fatorial") e é definido pela relação:
    m! = m.(m-1).(m-2).(m-3)...3.2.1, para m >= 2.

Algumas definições são:
    - 1! = 1 (fatorial de 1) - critério de parada
    - 0! = 1 (fatorial de 0)

Exemplos:
    3! = 3.2.1 = 6
    4! = 4.3.2.1 = 24
    6! = 6.5.4.3.2.1 = 720
'''

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(6))
