# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:39:55 2022

@author: vitu
"""

import re
texto = 'Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e meu site é https://www.iaexpert.academy http://iaexpert.com.br'

print(re.findall('\d', texto))
print(re.findall('\d{5}-\d{3}', texto))
print(re.findall('https?://[A-Za-z0-9./]+', texto))
