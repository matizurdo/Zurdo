import random
lista = []
for i in range(20):
    numero = random.randint(1,100)
    if numero not in lista:
        lista.append(numero)
print(lista)
