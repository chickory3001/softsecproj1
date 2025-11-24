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
        
        # Allow for PhoneNumber class to read phone numbers with hyphens.
        else:
            splitNum = phoneNum.split("-")
            assert len(splitNum) == 3, "improper use of hyphens"
            
            phoneNum = ""
            for nums in splitNum:
                phoneNum += nums
            
            assert len(phoneNum) == 10, "phone number length must be 10"
            assert phoneNum.isdecimal(), "phone number must be numbers"
            
        self._phoneNum = phoneNum
        
    
