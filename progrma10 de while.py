print("="*48)
print("Simular un cajero automático:")
print("="*48)
1
pc = "1234"
intentos_maximos = 3
intentos = 0

while intentos < intentos_maximos:
    pin = input("Ingrese su PIN: ")
    intentos += 1
    
    if pin == pc:
        print("PIN correcto. Acceso concedido.")
        break
    else:
        print("PIN incorrecto. Inténtelo nuevamente.")

if intentos == intentos_maximos:
    print("Ha excedido el número máximo de intentos permitidos. Tarjeta bloqueada.")