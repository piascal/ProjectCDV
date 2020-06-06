import unittest
from Tests.base_test import BaseTest
from Pages.main_page import MainPage
import time

mp = MainPage

class Test(BaseTest):

    def test_Cookie(self):
        print('Cookie Tests')
        mp.assertCookieText(self)
        time.sleep(2)
        mp.acceptCookies(self)


if __name__ == '__main__':
    unittest.main()