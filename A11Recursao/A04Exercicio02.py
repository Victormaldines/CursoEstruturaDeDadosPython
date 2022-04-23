'''
2. Crie uma função recursiva que calcule o valor de a (base) elevado a b (expoente)
    - Se o expoente for zero, a potência é igual 1 (critério de parada)
    - Não considere exponenciação de números negativos
'''

# 3^3 = 3.3.3 = 27
# 3^3 = 9.3 = 27
# 3^3 = 27 = 27

def exponenciacao(a, b):
    if b == 0:
        return 1
    else:
        return a * exponenciacao(a, b-1)

print(exponenciacao(3, 3))
