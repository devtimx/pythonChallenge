# Encrypt and decrypt text
from simplecrypt import encrypt, decrypt
import time
time.clock = time.time
def run():
    myText = input('Enter your text: ')
    passkey = 'secret'
    cipher = encrypt(passkey, myText)
    print(cipher)

    
    print(decrypt(passkey, cipher))

if __name__ == "__main__":
    run()