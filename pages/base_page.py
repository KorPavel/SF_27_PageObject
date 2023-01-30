from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url='https://petfriends.skillfactory.ru/login', timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        self.browser.get(self.url)

    def is_element_located(self, how, what):
        ''' Метод ищет элемент с явным ожиданием '''
        try:
            self.wait.until(
                EC.presence_of_element_located((how, what)),
                f'CSS Selector "\x1B[1m{what}\x1B[0m" is not find')
        except NoSuchElementException:
            return False
        return True

    def is_element_present(self, how, what):
        ''' Метод проверяет, что элемент присутствует на странице '''
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            print(f'Элемент с локатором {what} не найден')
            return False
        return True

    def is_elements_present(self, how, what):
        ''' Метод ищет группу элементов на странице по локаатору '''
        try:
            self.browser.find_elements(how, what)
        except NoSuchElementException:
            print(f'Элементы с локатором {what} не найдены')
            return False
        return True

