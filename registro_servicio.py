class Usuario:
    def __init__(self, nombre: str, email: str, password: str):
        self.nombre = nombre
        self.email = email
        self.password = password

class RegistroServicio:
    def registrar(self, nombre: str, email: str, password: str) -> Usuario:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if "@" not in email:
            raise ValueError("Email inválido")
        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")

        return Usuario(nombre, email, password)
