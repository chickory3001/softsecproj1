"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the AES_CBC module.
Test each method with at least one unit test.
"""

import unittest
from AES_CBC import *


# Define TestCheckingAccount class by extending the unittest.TestCase class
# Tests the checking account class 
class TestEncryption(unittest.TestCase):
    KEY = b'MySuperSecretKey2222222222222222'
    IV = b'MySuperSecretIV0'  
    PLAINTEXT = "This is my secret text\n   ffffflewfeauifeuwaihfieawo\n feuiowja\n"  
    DEBUG = False

    #tests encrypt and decrypt methods 
    def test_encryption(self):
        if TestEncryption.DEBUG:
            print("\nTesting encrypt and decrypt aes cbc methods ")

            # runs a plaintext through encryption and decryption
            ciphertext = encrypt_AES_CBC(TestEncryption.PLAINTEXT,TestEncryption.KEY,TestEncryption.IV)
            decrypted = decrypt_AES_CBC(ciphertext,TestEncryption.KEY,TestEncryption.IV)

            #checks if the plaintexts are the same before and after 
            self.assertEqual(decrypted,TestEncryption.PLAINTEXT)
    
    #tests encrypt asserts 
    def test_encrypt_asserts(self):
        if TestEncryption.DEBUG:
            print("\nTesting encrypt asserts ")
            # test data assert 
            with self.assertRaises(AssertionError):
                encrypt_AES_CBC(112312321,TestEncryption.KEY,TestEncryption.IV)
            
            #test key asserts 
            with self.assertRaises(AssertionError):
                encrypt_AES_CBC(TestEncryption.PLAINTEXT,1234123412341234,TestEncryption.IV)
            with self.assertRaises(AssertionError):
                encrypt_AES_CBC(TestEncryption.PLAINTEXT,b'123'.KEY,TestEncryption.IV)
            
            #test iv asserts
            with self.assertRaises(AssertionError):
                encrypt_AES_CBC(TestEncryption.PLAINTEXT,TestEncryption.KEY,1234123412341234)
            with self.assertRaises(AssertionError):
                encrypt_AES_CBC(TestEncryption.PLAINTEXT,TestEncryption.KEY,b'123')
    
    #tests decrypt asserts 
    def test_decrypt_asserts(self):
        if TestEncryption.DEBUG:
            print("\nTesting decrypt asserts ")
            # test ciphertext assert 
            with self.assertRaises(AssertionError):
                decrypt_AES_CBC(112312321,TestEncryption.KEY,TestEncryption.IV)
            
            #test key asserts 
            with self.assertRaises(AssertionError):
                decrypt_AES_CBC(TestEncryption.PLAINTEXT,1234123412341234,TestEncryption.IV)
            with self.assertRaises(AssertionError):
                decrypt_AES_CBC(TestEncryption.PLAINTEXT,b'123'.KEY,TestEncryption.IV)
            
            #test iv asserts
            with self.assertRaises(AssertionError):
                decrypt_AES_CBC(TestEncryption.PLAINTEXT,TestEncryption.KEY,1234123412341234)
            with self.assertRaises(AssertionError):
                decrypt_AES_CBC(TestEncryption.PLAINTEXT,TestEncryption.KEY,b'123')
