print("="*48)
print("Tabla de multiplicar:")
print("="*48)

numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)