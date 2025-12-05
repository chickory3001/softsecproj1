# Example of storing and retrieving Clients securely  - adapted from 
# https://www.askpython.com/python/examples/storing-retrieving-Clients-securely
# @author: Gurpreet Kaur / December 29, 2023
# @author: John McManus
# @date 11/08/2025

# import the required libraries
import os
import hashlib
from Password import Password

# Example Client class to demonstrate storing the required attributes to has passwords
class HashedPWD():
    
    # Client constructor
    # @parameter: password - the string passed in containing the password
    # @require: 8 <= len(password) <=  16
    # @require: password does not contain "/", "\", "<", ">", "|"    
    def __init__(self, password: Password, salt: bytes = os.urandom(16), pepper: bytes = os.urandom(16)):
        assert isinstance(password, Password), "Invalid password type"
        assert isinstance(salt, bytes), "Invalid salt type"
        assert isinstance(pepper, bytes), "Invalid pepper type"

        self._salt = salt
        self._pepper = pepper
        self._iterations = 100_000
        self._hash_algo = 'sha256'
        self._hashPWD = self._createSecureHash(password.getPassword())
    
    # return a string representation of the object   
    def __repr__(self):
        return ("\nIterations: %d, salt: %s, Algorithm: %s" % (self._iterations, self._salt, self._hash_algo))

    # Method to securly hash the password
    # @parameter: the password to hash
    # @require: 8 <= len(password) <=  16
    # @require: password does not contain "/", "\\", "<", ">", "|"
    
    def _createSecureHash(self, password):
        assert isinstance(password, str), "Invalid type"
        
        hash = hashlib.pbkdf2_hmac(
            self._hash_algo,
            password.encode('utf-8') + self._pepper.encode('utf-8'),  
            self._salt,
            self._iterations
        )  
        return hash
    
    # Private method to check a password against the stored hash
    # @parameter: password - the string passed in containing the password to check
    # @require: 8 <= len(password) <=  16
    # @require: password does not contain "/", "\\", "<", ">", "|"    
    
    def _checkPassword(self, password):
        #Assertions to check password type, length, and syntax
        assert isinstance(password, Password), "Invalid type"

        # Compute the hash from password entered   
        passwordHash = self._createSecureHash(password.getPassword())
        
        # Compare the computed hash and the stored hash and return the result
        return passwordHash == self._hashPWD
    
    # Tests equality between two hashedpwds
    # @ensure self is being compared to another hashedpwd
    # @return: True if equal, else False
    def __eq__(self,other):
        assert isinstance(other, HashedPWD)
        return self._hashPWD == other._hashPWD

