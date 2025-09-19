def registrar_usuario(usuario):
    # código mínimo para pasar la prueba
    if usuario.get("nombre") and usuario.get("email") and usuario.get("password"):
        return "Registro exitoso"
    else:
        return "Error en el registro"

