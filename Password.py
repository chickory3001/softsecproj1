"""
Password 

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Creates a password and checks to see if the password is valid, also resets when correct condentials have been fulfilled
"""

class Password:
  invalidPasswordChar = ["/", "\\", "<", ">", "|", "_"]

  def __init__(self, password):
    assert isinstance(password, str), "Invalid type"
    assert passwordChecker(password), "Invalid password"
    self._password = password    #Creates the password object

  # Method that will return the password
  def getPassword(self):
    return self._password
  
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
    while not passwordChecker(newPass):
      print("Password invalid try again:")
      newPass = input("Enter your new password")
      confirmPass = input("Enter your new password to confirm")

      while newPass != confirmPass:
        print("Passwords do not match try again:")
        newPass = input("Enter your new password")
        confirmPass = input("Enter your new password to confirm")


    self._password = newPass
    print("Password changed successfully")
    return True

