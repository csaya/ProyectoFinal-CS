import unittest
from registro import registrar_usuario

class TestRegistroUsuario(unittest.TestCase):
    def test_registro_exitoso(self):
        usuario = {"nombre": "Ana", "email": "ana@mail.com", "password": "1234"}
        resultado = registrar_usuario(usuario)
        self.assertEqual(resultado, "Registro exitoso")  # esperamos esta respuesta

if __name__ == '__main__':
    unittest.main()
