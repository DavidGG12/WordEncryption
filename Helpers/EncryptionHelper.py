from hashlib import blake2b
import os

class Encryption:
    def __init__(self):
        self.__keyWord:bytes = os.getenv("KeyWord").encode()

    def encrypt(self, word:str) -> str:
        KEY_WORD:bytes = self.__keyWord

        if KEY_WORD is None:
            KEY_WORD = b"palabraSecretaMuySecreta"
        
        h = blake2b(key = KEY_WORD, digest_size = 32)
        h.update(word)

        return h.hexdigest()
        

