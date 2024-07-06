print("="*46)
print("	Sumar dígitos de un número:")
print("="*46)

numero = int(input("Ingrese un número entero: "))
sd = 0

while numero > 0:
    sd += numero % 10
    numero //= 10

print("La suma de los dígitos del número es:", sd)
