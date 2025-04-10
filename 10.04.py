palabra=str (input("ingrese la palabra"))
vocal= "aeiou"
contador = 0

for letra in palabra:
    if letra in vocal:
        contador += 1

print("numero de vocales", contador)