from .base_page import BasePage
from .locators import AuthPageLocators
from selenium.webdriver.support import expected_conditions as EC


class AuthPage(BasePage):

    def should_be_login_field(self):
        assert self.wait.until(
            EC.url_to_be('https://petfriends.skillfactory.ru/login'),
            'Текущий URL не соответствует заявленному')
        self.should_be_title()
        self.should_be_email_field()
        self.should_be_password_field()
        self.should_be_submit_button()
        self.should_be_registration_link()

    def should_be_title(self):
        assert self.is_element_present(*AuthPageLocators.TITLE), \
            'Отсутствует заголовок сайта'
        assert self.wait.until(
            EC.presence_of_element_located(AuthPageLocators.TITLE)).text == 'PetFriends'

    def should_be_email_field(self):
        assert self.is_element_present(*AuthPageLocators.EMAIL_FIELD), \
            'Отсутствует поле ввода электронной почты'

    def should_be_password_field(self):
        assert self.is_element_present(*AuthPageLocators.PASSWORD_FIELD), \
            'Отсутствует поле ввода пароля'

    def should_be_submit_button(self):
        assert self.is_element_present(*AuthPageLocators.SUBMIT_BUTTON), \
            'Отсутствует кнопка ВОЙТИ'
        assert self.wait.until(
            EC.presence_of_element_located(
                AuthPageLocators.SUBMIT_BUTTON)).text == 'Войти'

    def should_be_registration_link(self):
        assert self.is_element_present(*AuthPageLocators.REGISTER_LINK), \
            'Отсутствует ссылка на страницу регистрации'
        assert self.wait.until(
            EC.presence_of_element_located(
                AuthPageLocators.REGISTER_LINK)).text == 'Зарегистрироваться'

    def guest_must_go_to_the_registration_page(self):
        reg_link = self.browser.find_element(*AuthPageLocators.REGISTER_LINK)
        reg_link.click()

    def send_auth_data(self, email, password):
        email_field = self.wait.until(
            EC.presence_of_element_located(AuthPageLocators.EMAIL_FIELD))
        email_field.send_keys(email)

        password_field = self.wait.until(
            EC.presence_of_element_located(AuthPageLocators.PASSWORD_FIELD))
        password_field.send_keys(password)

        submit_button = self.wait.until(
            EC.presence_of_element_located(AuthPageLocators.SUBMIT_BUTTON))
        submit_button.click()

        assert self.wait.until(
            EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'),
            'Текущий URL не соответствует заявленному')


