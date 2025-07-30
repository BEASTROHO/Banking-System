from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import base64

class AuthManager:
    def __init__(self, secret_key: str):
        self.key = PBKDF2(secret_key, b'static_salt', dkLen=32)

    def encrypt(self, plaintext: str) -> str:
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
        data = cipher.nonce + tag + ciphertext
        return base64.b64encode(data).decode()

    def decrypt(self, encrypted_text: str) -> str:
        raw = base64.b64decode(encrypted_text.encode())
        nonce = raw[:16]
        tag = raw[16:32]
        ciphertext = raw[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()

    def verify_password(self, input_password: str, stored_hash: str) -> bool:
        import hashlib
        return hashlib.sha256(input_password.encode()).hexdigest() == stored_hash
