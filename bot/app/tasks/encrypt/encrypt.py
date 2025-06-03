from cryptography.fernet import Fernet, InvalidToken
from app.models import singleton


@singleton
class Encrypt:
    def __init__(self):
        self._key = ""
        self.fernet = None

    def decrypt(self, data):
        if self.fernet is None:
            return None
        try:
            decrypted = self.fernet.decrypt(data)
            return decrypted
        except InvalidToken:
            return None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if isinstance(value, str):
            value = value.encode()
        self._key = value
        self.fernet = Fernet(self._key)
