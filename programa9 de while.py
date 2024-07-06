print("="*48)
print("	Convertir de decimal a binario:")
print("="*48)


decimal = int(input("Ingrese un número entero positivo: "))
binario = ""

while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal //= 2
    
print("el numero en binarioo es:",binario)