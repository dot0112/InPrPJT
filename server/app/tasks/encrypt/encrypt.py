from cryptography.fernet import Fernet
from app.models import singleton


@singleton
class Encrypt:
    def __init__(self):
        self._key = Fernet.generate_key()
        self.fernet = Fernet(self._key)

    def createKey(self):
        self.key = Fernet.generate_key()

    def encrypt(self, data):
        return self.fernet.encrypt(data)

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
        self.fernet = Fernet(self._key)
