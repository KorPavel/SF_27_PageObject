from .base_page import BasePage
from .locators import AllPetsPageLocators
from selenium.webdriver.support import expected_conditions as EC


class AllPetsPage(BasePage):

    def should_be_current_page(self):
        assert self.wait.until(
            EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'),
            'Текущий URL не соответствует заявленному')
        my_pets = self.wait.until(EC.presence_of_element_located(
            AllPetsPageLocators.MY_PETS))
        my_pets.click()
        assert self.wait.until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'),
                               'Текущий URL не соответствует заявленному')