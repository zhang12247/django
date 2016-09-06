from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class DESUtil:
    def __init__(self):
        self.key = "abcdefghijklmnop"
        self.mode = AES.MODE_CBC

    def encrypt(self, password):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(password)
        add = length - (count % length)
        password = password + ('\0' * add)
        self.ciphertext = cryptor.encrypt(password)
        return b2a_hex(self.ciphertext).decode()

    def my_decrypt(self, password):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(password))
        plain_text = plain_text.decode().rstrip('\0')
        print(plain_text)
        # return plain_text.rstrip('\0')


