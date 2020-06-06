from selenium.webdriver.common.by import By

class MainPageLocators():
    ACCEPT_COOKIES = (By.CSS_SELECTOR, '.optanon-alert-box-button-middle > .optanon-allow-all')
    COOKIES_MESSAGE = (By.ID, 'alert-box-message')
    LOCALIZATION_INPUT = (By.ID, 'bigsearch-query-attached-query')
    DATE = (By.CLASS_NAME, '_y6t6ipn')
    DATE_START = (By.XPATH, '//td[@class="_12fun97"][@role="button')