print("="*50)
print("	Convertir grados Celsius a Fahrenheit:")
print("="*50)


i = int(input("Ingresa la temperatura inicial en grados Celsius: "))
f = int(input("Ingresa la temperatura final en grados Celsius: "))

print("\nConversión de grados Celsius a Fahrenheit:")

for celsius in range(i, f + 1):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
