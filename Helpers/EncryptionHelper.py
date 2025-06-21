from cryptography.fernet import Fernet
import os

class Encryption:
    def __init__(self):
        self.__keyWord:bytes = os.getenv("KeyWord").encode()

    def encrypt(self, word:str) -> str:
        KEY_WORD:bytes = self.__keyWord

        if KEY_WORD is None or (len(KEY_WORD) * 8) <= 32:
            KEY_WORD = Fernet.generate_key()

        f = Fernet(KEY_WORD)
        wordEncrypt = f.encrypt(word.encode()).decode()

        return wordEncrypt

    def decrypt(self, word:str) -> str:
        KEY_WORD:bytes = self.__keyWord

        if KEY_WORD is None or (len(KEY_WORD) * 8) <= 32:
            KEY_WORD = Fernet.generate_key()

        f = Fernet(KEY_WORD)
        wordEncrypt = f.decrypt(word.encode()).decode()

        return wordEncrypt

m = Encryption()
x = m.encrypt("IanDavidGarciaGarcia2025")

print(x)
print(m.decrypt(x))
        
