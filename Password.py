"""
Password 

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Creates a password and checks to see if the password is valid, also resets when correct condentials have been fulfilled
"""

class Password:
  invalidPasswordChar = ["/", "\\", "<", ">", "|", "_"]

  def __init__(self, password):
    assert passwordChecker(password), "Invalid password"
    self._password = password    #Creates the password object
  
  #Sets password, goes throught a while loop to check if the password is valid within the parameters
  #@Require Password being set is valid
  #@Ensure Password is saved to the client's account
  def passwordChecker(self, userPassword):
    for character in Password.invalidPassswordChar:
      if character in userPassword:
        return False

      if len(userPassword) < 8 or len(userPassword) > 16:
        return False
    return True
    
  #Changes the password the user wants to enter
  #@Require Password is already associated with an account
  #@Ensure Password is being changed
  def changePassword(self):
    oldPass = input("Enter your previous password")  #Check previous password
    if oldPass != self._password:
      print("Incorrect Previous Password:")
      return False

    #Creation of new password and confirm password
    newPass = input("Enter your new password")
    confirmPass = input("Enter your new password to confirm")
    
    #If the passwords don't match try again
    while newPass != confirmPass:
      print("Passwords do not match try again:")
      newPass = input("Enter your new password")
      confirmPass = input("Enter your new password to confirm")

    
    #Checks new password to see if it is valid, if not prompt the user to try again
    while not self.isValid(newPass):
      newPass = input("Enter your new password")
      confirmPass = input("Enter your new password to confirm")

      while newPass != confirmPass:
        print("Passwords do not match try again:")
        newPass = input("Enter your new password")
        confirmPass = input("Enter your new password to confirm")


    self._password = newPass
    print("Password changed successfully")
    return True


  # Method to securly hash the password
    # @parameter: the password to hash
    # @require: 8 <= len(password) <=  16
    # @require: password does not contain "/", "\\", "<", ">", "|"
  def _createSecureHash(self, password):
      assert isinstance(password, str), "Invalid type"
      assert Client.PASS_MIN_LEN <= len(password) <=  Client.PASS_MAX_LEN, "Invalid length" 
      assert _checkSyntax(password)
        
      # Create a random 16 byte salt
      self._salt = os.urandom(16)
      self._iterations = 100_000
      self._hash_algo = 'sha256'
      self._hash = hashlib.pbkdf2_hmac(
        self._hash_algo,
        password.encode('utf-8') + Client.PEPPER.encode('utf-8'),  
        self._salt,
        self._iterations
      )  
    
    # Private method to check a password against the stored hash
    # @parameter: password - the string passed in containing the password to check
    # @require: 8 <= len(password) <=  16
    # @require: password does not contain "/", "\\", "<", ">", "|"    
  def _checkPassword(self, password):
    #Assertions to check password type, length, and syntax
    assert isinstance(password, str), "Invalid type"
    assert Client.PASS_MIN_LEN <= len(password) <=  Client.PASS_MAX_LEN, "Invalid length" 
    assert _checkSyntax(password)

    # Compute the hash from password entered   
    passswordHash = hashlib.pbkdf2_hmac(
      self._hash_algo, 
      password.encode('utf-8') + Client.PEPPER.encode('utf-8'),  
      self._salt,
      self._iterations
      )
         
    # Compare the computed hash and the stored hash and return the result
    return (passswordHash == self._hash)

