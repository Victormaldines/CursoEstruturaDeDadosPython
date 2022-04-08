a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = a + b + [9, 10]
res = []

"""
# A ^ ~ B
for item in c:
    if item in a and not(item in b):
        res.append(item)
print(set(res))
"""

"""
# ~A ^  B
for item in c:
    if not(item in a) or item in b:
        res.append(item)
print(set(res))
"""

"""
# ~A v ~B
for item in c:
    if not(item in a) or not(item in b):
        res.append(item)
print(set(res))
"""

"""
# ~A ^ ~B
for numero in c:
    if not(numero in a) and not(numero in b): # 
        res.append(numero)
print(set(res))
"""      


for numero in c:
    if numero in a or not(numero in b):
        res.append(numero)
print(set(res))
