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
    userPassword = scan("Enter a pasword between 8 - 16 characters:")
    passwordCheck = invalidPasswordChar[0]
    while userPassword != "":
      if userPassword == invalidPasswordChar[passwordCheck]:
        print("Invalid Character", invalidPasswordChar[passwordCheck])
      else:
      userPassword == True
    
    
    
