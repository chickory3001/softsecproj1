# PhoneNumber.py
# 
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 3
# 
# This module defines the PhoneNumber class.
# A simple class to hold a phone number.

class PhoneNumber:
    
    def __init__(self, phoneNum: str):
        assert isinstance(phoneNum, str), "phone number must be a string"
        
        if phoneNum.isdecimal():
            assert len(phoneNum) == 10, "phone number length must be 10"
            assert not phoneNum[0] in ["0", "1", "2"], "phone number can't begin with 0, 1, or 2"

        
        # Allow for PhoneNumber class to read phone numbers with hyphens.
        # else:
        #     splitNum = phoneNum.split("-")
        #     assert len(splitNum) == 3, "improper use of hyphens"
        #     phoneNum = "".join(splitNum)
            
        #     assert len(phoneNum) == 10, "phone number length must be 10"
        #     assert phoneNum.isdecimal(), "phone number must be numbers"
        
        self._phoneNum = phoneNum
    
    #getter for phonenum
    #returns phone number as string 
    def getPhoneNum(self) -> str:
        return self._phoneNum
    
    # equality method 
    # @ensure other is a phonenumber 
    # returns true if the two phoe number strings are equal, false if not 
    def __eq__(self,other: 'PhoneNumber') -> bool:
        assert isinstance(other, PhoneNumber), "Invalid comparison"
        return self._phoneNum == other._phoneNum