# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:50:35 2022

@author: vitu

1. Ler 5 notas e informar a média:
"""

# FOR
somaNotas = 0
for i in range(0, 5):
    somaNotas += float(input(f'Informe a {i+1}ª nota: '))
media = somaNotas / 5
print(media)


"""
# WHILE
count = somaNotas2 = 0
while count < 5:
    somaNotas2 += float(input(f'Informe a {count+1}ª nota: '))
    count += 1
media = somaNotas2 / 5
print(media)
"""