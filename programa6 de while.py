print("="*48) 
print("	Mostrar múltiplos de un número:")
print("="*48)

numero = int(input("Ingrese un número entero positivo: "))
contador = 1

while contador <= 10:
    print(numero * contador)
    contador += 1
