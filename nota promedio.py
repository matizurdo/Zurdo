def evaluar(nombre, nota1, nota2):
    promedio=(nota1+nota2) /2 
    
    if promedio >= 6:
        return f"{nombre} aprobo con {promedio}"
    else:
            return f"{nombre} deseprobo con {promedio}"

resultado=evaluar("Matias",10,9)
print(resultado)