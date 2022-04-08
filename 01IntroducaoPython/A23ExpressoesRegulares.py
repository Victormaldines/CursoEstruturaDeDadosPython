# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:54:41 2022

@author: vitu

EXPRESSÕES REGULARES
MÉTODOS
    SEARCH: encontrar as posições de padrões dentro de uma string, se estes
    estiverem presentes
    
    MATCH: Encontrar se o começo de uma string é igual a um determinado padrão
    
    FINDALL: Encontrar todas as substrings em uma string que correspondem a um
    padrão
 
METACARACTERES
.  - Qualquer caractere (exceto linha nova)
\w - Qualquer caractere alfanumérico
\W - Qualquer caractere não-alfanumérico
\d - Qualquer caractere que seja um digito (0-9)
\D - Qualquer caractere que não seja um digito
\s - Espaço em branco
^  - começa com
$  - termina com
"\"- Usado antes de metacaracteres para espeficiar seu significado literal

QUANTIFICADORES
Permitem determinar como e quantas vezes os metacaracteres aparecem
[] - opcional entre os que estão dentro dos colchetes
() - captura grupos de caracteres
*  - de zero a mais vezes
?  - de zero ou uma vez
+  - de uma ou mais vezes
{m,n} - de m a n vezes
| - ou

EXEMPLOS
gabrielcosta@hotmail.com
felipearruda@gmail.com
joaosilva@yahoo.com.br

Expressão regular que detecta emails: \w+@\w+\.\w+
"""

import re # Regular Expression

# MÉTODO SEARCH(<regExp>, <string>)
frase1 = 'Olá, meu número de telefone é (42)0000-0000'
#print(re.search('\(\d{2}\)?\d{4,5}-\d{4}', frase1))

frase2 = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'

#print(re.search('[A-Za-z]{3}-\d{4}', frase2))

email = 'Entre em contato, meu email é teste@teste.com'
#print(re.search('\w+@\w+\.\w+', email))

# MÉTODO MATCH
frase1 = 'A placa de carro que eu anotei durante a batida foi FRT-1998'
#print(re.match('[A-Za-z]{3}-\d{4}', frase1))
frase2 = 'FRT-1998 é a placa do carro'
#print(re.match('[A-Za-z]{3}-\d{4}', frase2))

# MÉTODO FINDALL
frase3 = 'Meu número de telefone atual é (42)0000-0000. O número (56)11111-1111 é o antigo'

print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3))

emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com
'''

print(re.findall('\w+@\w+\.\w*', emails))
