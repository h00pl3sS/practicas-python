diccionario = {
    "admin" : "admin123",
    "root" : "toor",
    "analyst" : "password"
}

intentosDiccionario = []
intentos = 0

def validar(usuario, contraseña):
    return usuario in diccionario and diccionario[usuario] == contraseña

def registrar_intento(usuario, contraseña):
    intentosDiccionario.append(f"Usuario {usuario}, Contraseña: {contraseña}")

while intentos < 3:
    usuario = input("Introduce tu usuario: ")
    contraseña = input("Introduce tu contraseña: ")

    if validar(usuario, contraseña):
        print(f"Bienvenido {usuario}")
        break
    else:
        print("Credenciales incorrectas")
        registrar_intento(usuario, contraseña)
        intentos += 1

if intentos == 3:
    print("Cuenta bloqueada, contacta con el administrador")
    print("Intentos fallidos: ")
    for intento in intentosDiccionario:
        print("-", intento)
