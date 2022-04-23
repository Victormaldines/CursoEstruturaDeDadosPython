'''
RECURSÃO 01
MOSTRAR MENSAGENS
'''

# loop for
for _ in range(5):
    print('Recursão')

print()

# recursão
def recursao(i):
    print('Recursão')
    i += 1
    if i == 5:
        return
    else:
        recursao(i)

recursao(0)
