print("="*48)
print("	Sumar los primeros N números naturales:")
print("="*48)


N = int(input("Ingresa un número entero positivo: "))


if N > 0:
    suma = 0

    for i in range(1, N + 1):
        suma += i
        
        
    print(f"La suma de los primeros {N} números naturales es:", suma)
else:
    print("El número ingresado no es positivo.")
