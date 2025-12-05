"""
Password 

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Creates a password and checks to see if the password is valid, also resets when correct condentials have been fulfilled
"""

class Password:
  invalidPasswordChar = {"/", "\\", "<", ">", "|"}

  def __init__(self, password: str):
    assert self.passwordChecker(password), "Invalid password"
    self._password = password    #Creates the password object

  # Method that will return the password
  def getPassword(self):
    return self._password
  
  #Sets password, goes throught a while loop to check if the password is valid within the parameters
  #@Require Password being set is valid
  #@Ensure Password is saved to the client's account
  def passwordChecker(self, userPassword):
    if not isinstance(userPassword,str):
      return False
    for character in Password.invalidPasswordChar:
      if character in userPassword:
        return False

      if len(userPassword) < 8 or len(userPassword) > 16:
        return False
    return True
