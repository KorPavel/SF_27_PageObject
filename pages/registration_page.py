from .base_page import BasePage
from .locators import RegPageLocators
from selenium.webdriver.support import expected_conditions as EC


class RegPage(BasePage):

    def should_be_registration_field(self):
        assert self.wait.until(
            EC.url_to_be('https://petfriends.skillfactory.ru/new_user'),
            'Текущий URL не соответствует заявленному')
        self.should_be_title()
        self.should_be_name_field()
        self.should_be_email_field()
        self.should_be_password_field()
        self.should_be_submit_button()
        self.should_be_registration_link()

    def should_be_title(self):
        assert self.is_element_present(*RegPageLocators.TITLE), \
            'Отсутствует заголовок сайта'
        assert self.wait.until(
            EC.presence_of_element_located(
                RegPageLocators.TITLE)).text == 'PetFriends'

    def should_be_name_field(self):
        assert self.is_element_present(*RegPageLocators.NAME_FIELD), \
            'Отсутствует поле ввода уникального имени'

    def should_be_email_field(self):
        assert self.is_element_present(*RegPageLocators.EMAIL_FIELD), \
            'Отсутствует поле ввода электронной почты'

    def should_be_password_field(self):
        assert self.is_element_present(*RegPageLocators.PASSWORD_FIELD), \
            'Отсутствует поле ввода пароля'

    def should_be_submit_button(self):
        assert self.is_element_present(*RegPageLocators.SUBMIT_BUTTON), \
            'Отсутствует кнопка "Зарегистрироваться"'
        assert self.wait.until(
            EC.presence_of_element_located(
                RegPageLocators.SUBMIT_BUTTON)).text == 'Зарегистрироваться'

    def should_be_registration_link(self):
        assert self.is_element_present(*RegPageLocators.LOGIN_LINK), \
            'Отсутствует ссылка на страницу Входа в аккаунт'
        assert self.wait.until(
            EC.presence_of_element_located(
                RegPageLocators.LOGIN_LINK)).text == 'У меня уже есть аккаунт'

    def guest_must_go_to_the_login_page(self):
        reg_link = self.browser.find_element(*RegPageLocators.LOGIN_LINK)
        reg_link.click()