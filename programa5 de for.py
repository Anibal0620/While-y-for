print("="*48)
print("	Imprimir números impares:")
print("="*48)


numero = int(input("Ingresa un número entero positivo: "))

if numero > 0:
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i)
else:
    print("El número ingresado no es positivo.")
