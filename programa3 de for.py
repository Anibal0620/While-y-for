print("="*48)
print("	Contar vocales en una cadena:")
print("="*48)


cadena = input("Ingresa una cadena de texto: ")

cv = 0

vocales = "aeiouAEIOU"

for caracter in cadena:
    if caracter in vocales:
        cv += 1


print("El número de vocales en la cadena es:", cv)
