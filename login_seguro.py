diccionario = {
    "admin" : "admin123",
    "root" : "toor",
    "analyst" : "password"
}

intentosDiccionario = []
intentos = 0

while intentos < 3:
    usuarioLogin = input("Introduce tu usuario: ")
    usuarioPassword = input("Introduce tu contraseña: ")

    if usuarioLogin in diccionario and diccionario[usuarioLogin] == usuarioPassword:
        print(f"Bienvenido {usuarioLogin}")
        break
    else:
        print("Credenciales incorrectas")
        intentosDiccionario.append(f"Usuario {usuarioLogin}, Contraseña: {usuarioPassword}")
        intentos += 1

if intentos == 3:
    print("Cuenta bloqueada, contacta con el administrador")
    print("Intentos fallidos: ")
    for intento in intentosDiccionario:
        print("-", intento)