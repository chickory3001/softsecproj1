# https://techexpert.tips/python/python-using-aes-encryption/#google_vignette
# Code to implement AES CBC encryption
# @date 10-19-2025

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Function to encrypt using AES in CBC mode
# @parameter data: The text to decrypt
# @parameter key: the key to decrypt the ciphertext
# @parameter iv: The initialization vector
def encrypt_AES_CBC(data: str, key: bytes, iv: bytes) -> bytes:
    assert isinstance(data,str)
    assert isinstance(key,bytes) and len(key) in [16,24,32]
    assert isinstance(iv,bytes) and len(iv) == 16
    padder = padding.PKCS7(128).padder()  
    padded_data = padder.update(data.encode('utf-8'))  
    padded_data += padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())  
    encryptor = cipher.encryptor()  
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()  
    return ciphertext

# Function to decrypt using AES in CBC mode
# @parameter ciphertext: The ciphertext to decrypt
# @parameter key: the key to decrypt the ciphertext
# @parameter iv: The initialization vector
def decrypt_AES_CBC(ciphertext: bytes, key: bytes, iv: bytes) -> str:
    assert isinstance(ciphertext,bytes)
    assert isinstance(key,bytes) and len(key) in [16,24,32]
    assert isinstance(iv,bytes) and len(iv) == 16
    decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()  
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize() 
    unpadder = padding.PKCS7(128).unpadder()  
    unpadded_data = unpadder.update(decrypted_data)  
    unpadded_data += unpadder.finalize()
    return unpadded_data.decode('utf-8')  

# if __name__ == '__main__':
#     # Encryption key (Ensure the key is 16, 24, or 32 bytes for AES-128, AES-192, or AES-256)
#     key = b'MySuperSecretKey2222222222222222'  
#     # Initialization vector (Ensure the IV is 16 bytes)
#     iv = b'MySuperSecretIV0'  
#     plaintext = "This is my secret text\n   ffffflewfeauifeuwaihfieawo\n feuiowja\n"  
#     print(f'Plain text: {plaintext}')
    
#     # Encrypt the plaintext
#     encrypted_text = encrypt_AES_CBC(plaintext, key, iv)  
#     print(f'Encrypted text: {encrypted_text}')
    
#     # write raw bytes to text file 
#     with open("checking.txt", "wb") as f:
#         f.write(encrypted_text)

#     # read raw bytes back
#     with open("checking.txt", "rb") as f:
#         filedata = f.read()

#     # Decrypt the encrypted text
#     decrypted_text = decrypt_AES_CBC(filedata, key, iv)
#     print(f'Decrypted text: {decrypted_text}')