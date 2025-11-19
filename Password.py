"""
Password 

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Creates a password and checks to see if the password is valid
"""
from ClientHash import Client


invalidPasswordChar = ["/", "\", "<", ">", "|", "_"]
#Creates the password object
class Password:
  def __init__(self):
    self._password = password
  
  #Asks user for a password to enter, make it go through the Client Hash written by the professor to check
  def passwordChecker(self):
    self._password = scan("Enter a password between 8 - 16 characters:")
    passwordCheck = invalidPasswordChar[0]
    
    #Checks the userPassword with the list of invalid password characters
    while self._password != "":
      if self._password == invalidPasswordChar[passwordCheck]:
        print("Invalid Character", invalidPasswordChar[passwordCheck])
      else:
      self._password == True

    def changePassword(self):
      userPassword = scan("Enter the previous password")
      if self._password != userPassword:  #Returns false if the previous password isn't entered correctly
        return False
      else:
        userPassword = scan("Enter your new password betweeen 8 - 16 characters)
        passwordConfrim = scan("Enter your password again to confirm")
        if userPassword != passwordConfrim:  #If the new passwords aren't the same then it will deny the changes
          print("Incorrect password")
        else:
          self._password = userPassword  #Resets to the new password
        
        
      
      
    
    
    
