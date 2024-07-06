print("="*48)
print("	5Determinar si un número es primo:")
print("="*48)


numero = int(input("Ingresa un número entero positivo: "))



if numero > 1:

    esp = True

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False

    if esp:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
else:
    print("El número ingresado no es mayor que 1 o no es positivo.")