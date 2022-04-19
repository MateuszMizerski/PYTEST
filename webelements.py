from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WebElements():

    def __init__(self, driver, id: str = '', xpath: str = ''):
        self.driver = driver
        self.id = id
        self.xpath = xpath

    @property
    def get_selector(self):
        return By.ID if self.id else By.XPATH

    def click(self):
        obj = self.driver.find_element(by=self.get_selector, value=self.id or self.xpath)
        obj.click()

    def wait_until_element_visible(self, timeout: int=30):
        locator = (self.get_selector, self.id or self.xpath)
        element = WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator=locator))


class Input(WebElements):

    def set_text(self, text):
        input = self.driver.find_element(by=self.get_selector, value=self.id or self.xpath)
        input.click()
        input.clear()
        input.send_keys(text)


class Portal:
    """class to test register form"""
    def __init__(self, url: str = 'http://care.pureinteractive.pl/?mod=signUp'):
        self.url = url
        self._webdriver = webdriver.Chrome()
        self._name_obj = Input(self._webdriver, 'name')
        self._last_name_obj = Input(self._webdriver, 'lastName')
        self._phone_obj = Input(self._webdriver, 'phone')
        self._email_obj = Input(self._webdriver, 'email')
        self._phone_marketing_agreement_obj = WebElements(self._webdriver, xpath='//input[@name="marketing_consents_16"]')
        self._email_marketing_agreement_obj = WebElements(self._webdriver, xpath='//input[@name="marketing_consents_15"]')
        self._submit_button_obj = WebElements(self._webdriver, xpath='//button[@type="submit"]')
        self._success_page_popup_obj = WebElements(self._webdriver, xpath='//h4[contains(.,"Na Twój adres email wysłaliśmy link do aktywacji konta")]')
        self._register_page_popup_obj = WebElements(self._webdriver, xpath='//h4[contains(.,"Zarejestruj się, aby wypełnić ankietę")]')
        

    def open_browser(self):
        self._webdriver.get(self.url)
        self._webdriver.maximize_window()

    def go_to_register_page(self):
        self._webdriver.get(self.url)

    def close_browser(self):
        self._webdriver.quit()
    
    def register_page_is_visible(self):
        self._register_page_popup_obj.wait_until_element_visible()

    def success_page_is_visible(self):
        self._success_page_popup_obj.wait_until_element_visible()

    def success_page_is_not_visible(self):
        try:
            self._success_page_popup_obj.wait_until_element_visible(timeout=15)
        except TimeoutException:
            pass

    def set_name(self, name: str):
        self._name_obj.set_text(name)
    
    def set_last_name(self, lastname: str):
        self._last_name_obj.set_text(lastname)

    def set_phone(self, phone: str):
        self._phone_obj.set_text(phone)
    
    def set_email(self, email: str):
        self._email_obj.set_text(email)
    
    def mark_phone_marketing_agrement(self):
        self._phone_marketing_agreement_obj.click()
    
    def mark_email_marketing_agrement(self):
        self._email_marketing_agreement_obj.click()
    
    def click_register(self):
        self._submit_button_obj.click()  
