'''
2. Crie uma função recursiva que calcule o valor de a (base) elevado a b (expoente)
    - Se o expoente for zero, a potência é igual 1 (critério de parada)
    - Não considere exponenciação de números negativos
'''

def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)

print(potencia(2, 2))
print(potencia(2, 3))
print(potencia(2, 4))