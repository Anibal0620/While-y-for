print("="*46)
print("Adivinar un número:")
print("="*46)

import random

na = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1
    
    if intento < na:
        print("El número es mayor.")
    elif intento > na:
        print("El número es menor.")
    else:
        print("¡Adivinaste en", intentos, "intentos!")
        break
