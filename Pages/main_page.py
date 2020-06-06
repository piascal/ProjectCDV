from selenium.common.exceptions import NoSuchElementException
from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



class MainPage():

    def assertCookieText(self):
        try:
            el = self.driver.find_element(*MainPageLocators.COOKIES_MESSAGE)
            assert el.text == 'Używamy plików cookie, aby spersonalizować treść, dostosować i zmierzyć reklamy oraz zapewnić bezpieczeństwo. Korzystając ze strony, wyrażasz zgodę na wykorzystywanie plików cookie do gromadzenia informacji na Airbnb i poza nim. Przeczytaj naszą Politykę plików cookie, aby dowiedzieć się więcej lub przejdź do zakładki „Ustawienia plików cookie”, aby zarządzać ustawieniami.'
        except NoSuchElementException:
            print('CookieText not foud')

    def acceptCookies(self):
        try:
            el = self.driver.find_element(*MainPageLocators.ACCEPT_COOKIES)
            el.click()
        except NoSuchElementException:
            print('Accept cookie btn not found')
