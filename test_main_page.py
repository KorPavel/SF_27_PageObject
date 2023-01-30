import pytest
from .pages.auth_page import AuthPage
from .pages.registration_page import RegPage
from .pages.all_pets_page import AllPetsPage
from .pages.my_pets_page import MyPetsPage
from settings import valid_email, valid_password, valid_user_name, new_pet


def test_guest_should_see_login_field(browser):
    """ Тест-кейс гость проверяет наличие основных
    элементов на странице входа """
    page = AuthPage(browser)
    page.open()
    page.should_be_login_field()


def test_guest_must_go_to_the_registration_page(browser):
    """ Гость переходит на страницу регистрации и проверяет
    наличие основных элементов на этой странице"""
    page = AuthPage(browser)
    page.open()
    page.guest_must_go_to_the_registration_page()
    reg_page = RegPage(browser, browser.current_url)
    reg_page.should_be_registration_field()


class TestUserLoginSelfAccount:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """ Пользователь логинится на сайте """
        page = AuthPage(browser)
        page.open()
        page.send_auth_data(valid_email, valid_password)

    def test_user_checks_the_amount_of_his_pets(self, browser):
        """ Пользователь проверяет количество своих питомцев с таблицей,
        процент карточек питомцев с фото, заполненность полей (имя, порода, возраст)
        в карточках питомцев, уникальность имён питомцев, повторяющиеся карточки """
        allpets_page = AllPetsPage(browser, browser.current_url)
        allpets_page.open()
        allpets_page.should_be_current_page()
        my_pets_page = MyPetsPage(browser, browser.current_url)
        my_pets_page.is_correct_user_name(valid_user_name)
        my_pets_page.get_my_pets_amount_before()
        my_pets_page.checks_the_amount_of_his_pets()


    def test_user_adding_new_pet(self, browser):
        """ Пользователь добавляет карточку нового питомца без фото """
        allpets_page = AllPetsPage(browser, browser.current_url)
        allpets_page.open()
        allpets_page.should_be_current_page()
        my_pets_page = MyPetsPage(browser, browser.current_url)
        my_pets_page.is_correct_user_name(valid_user_name)
        my_pets_page.get_my_pets_amount_before()
        my_pets_page.add_new_pet(new_pet)

    def test_user_delete_last_pet(self, browser):
        """ Пользователь удаляет карточку последнего питомца """
        allpets_page = AllPetsPage(browser, browser.current_url)
        allpets_page.open()
        allpets_page.should_be_current_page()
        my_pets_page = MyPetsPage(browser, browser.current_url)
        my_pets_page.is_correct_user_name(valid_user_name)
        my_pets_page.get_my_pets_amount_before()
        my_pets_page.delete_last_pet()