

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cryptography.fernet import Fernet

class Encriptacion:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encriptar(self, texto):
        return self.cipher_suite.encrypt(texto.encode()).decode()

    def desencriptar(self, texto_encriptado):
        return self.cipher_suite.decrypt(texto_encriptado.encode()).decode()

    def comparar(self, texto_original, texto_encriptado):
        return texto_original == self.desencriptar(texto_encriptado)

