with open('./frase1.txt') as txt:
    for linha in txt:
        print(linha)

with open('./frase1.txt') as txt:
    r = txt.readlines()
    
print(r)

with open('./texto2.txt', 'w') as txt:
    txt.write('Ola a todos')
    
with open('./texto2.txt', 'r') as txt:
    for linha in txt:
        print(linha)
        