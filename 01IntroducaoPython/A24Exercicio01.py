# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:31:18 2022

@author: vitu

1. Crie expressões regulares para extrair as seguintes informações do texto
abaixo (use a função findall)
- Números
- CEPs
- URLs
"""

import re

frase = 'Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e meu site é https://www.iaexpert.academy'

regNumeros = '\d+'
regCeps = '\d{5}-\d{3}'
regUrls = '(http(s)?://)?w{3}\.\w+\.\w+'


print(re.findall(regNumeros, frase))
print(re.search(regCeps, frase))
print(re.search(regUrls, frase))
