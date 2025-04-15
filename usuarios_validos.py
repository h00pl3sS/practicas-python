usuariosPermitidos = ["admin", "root", "analyst"]
usuarioLogin = input("Introduce un nombre de usuario: ").lower()

if usuarioLogin in usuariosPermitidos:
    print("Usuario válido, accediendo al sistema...")
else:
    print("Usuario no autorizado")