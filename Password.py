"""
Password 

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Creates a password and checks to see if the password is valid, also resets when correct condentials have been fulfilled
"""
from ClientHash import Client


invalidPasswordChar = ["/", "\", "<", ">", "|", "_"]
#Creates the password object
class Password:
  def __init__(self):
    self._password = password
  
  #Sets password, goes throught a while loop to check if the password is valid within the parameters
  #@Require Password being set is valid
  #@Ensure Password is saved to the client's account
  def passwordChecker(self):
    self._password = scan("Enter a password between 8 - 16 characters:")
    passwordCheck = invalidPasswordChar[0]
    
    #Checks the userPassword with the list of invalid password characters
    while self._password != "":
      if self._password == invalidPasswordChar[passwordCheck]:  #Prints why it fails, special characters that can't be used
        print("Invalid Character", invalidPasswordChar[passwordCheck])
      elif len(self._password) < 8 and len(self._password) > 16:  #Prints why it fails, doesn't follow length requirements
        print("Password length isn't valid, needs to be between 8 - 16 characters:")
      else:
      self._password == True    #Saves Password

    
    #Changes the password the user wants to enter
    #@Require Password is already associated with an account
    #@Ensure Password is being changed
    def changePassword(self):
      userPassword = scan("Enter the previous password")
      if self._password != userPassword:  #Returns false if the previous password isn't entered correctly
        return False
      else:
        userPassword = scan("Enter your new password betweeen 8 - 16 characters")
        passwordConfrim = scan("Enter your password again to confirm")
        
        if userPassword != passwordConfrim:  #If the new passwords aren't the same then it will deny the changes
          print("Incorrect password")
        
        else:
          while userPassword !=:  #Redo the while loop from earlier, to verify the password being changed follows the right parameters
          if userPassword == invalidPasswordChar[passwordCheck]:
            print("Invalid Character", invalidPasswordChar[passwordCheck])
          elif len(userPassword) < 8 and len(userPassword) > 16:
            print("Password length isn't valid, needs to be between 8 - 16 characters")
          else:
            self._password = userPassword  #Resets to the new password
        
        
      
      
    
    
    
