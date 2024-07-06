print("="*48)
print("	Dibujar un triángulo de asteriscos:")
print("="*48)


N = int(input("Ingresa un número entero positivo para la altura del triángulo: "))
 

if N > 0:
    for i in range(1, N + 1):
        print('*' * i)
else:
    print("El número ingresado no es positivo.")
