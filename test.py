"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the Client module.
Test each method with at least one unit test.
"""

import unittest
from Client import Client
from Address import Address

class TestClient(unittest.TestCase):
    #Constants
    FIRSTNAME = 'timmy'
    LASTNAME = 'smith'
    PHONE= 9123456789
    ADDRESS = Address('timmydrive','glenallen','VA')
    DEBUG = False

    # The setup method craetes a client
    def setUp(self):
        self.client1 = Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'), 'checking')
