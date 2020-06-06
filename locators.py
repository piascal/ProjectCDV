from selenium.webdriver.common.by import By

class MainPageLocators():
    ACCEPT_COOKIES = (By.CSS_SELECTOR, '.optanon-alert-box-button-middle > .optanon-allow-all')
    COOKIES_MESSAGE = (By.ID, 'alert-box-message')