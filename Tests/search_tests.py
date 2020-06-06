import unittest
from Tests.base_test import BaseTest
from Pages.main_page import MainPage
import time

mp = MainPage

class Test(BaseTest):
    def test_case1(self):
        print('Test Case 2: Sprawdzanie wyników po lokalizacji - Karpacz')
        mp.type_destination(self)
        mp.select_date(self)
        mp.select_date(self)





if __name__ == '__main__':
    unittest.main()