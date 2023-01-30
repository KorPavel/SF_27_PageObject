from .base_page import BasePage
from .locators import MyPetsPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MyPetsPage(BasePage):

    def should_be_current_page(self):
        assert self.wait.until(
            EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'),
            'Текущий URL не соответствует заявленному')

    def is_correct_user_name(self, name):
        assert self.wait.until(EC.presence_of_element_located(
            MyPetsPageLocators.USER_NAME)).text == name

    def get_my_pets_amount_before(self):
        page_info = self.wait.until(EC.presence_of_element_located(
            MyPetsPageLocators.PAGE_INFO)).text
        self.pets_amount_before = int(page_info.split(': ')[1].split('\n')[0])
        print(f'\nКоличество моих питомцев: {self.pets_amount_before}')

    def checks_the_amount_of_his_pets(self):
        my_pets_tabl = self.wait.until(EC.presence_of_all_elements_located(
            MyPetsPageLocators.MY_PETS_TABL))
        list_my_pets = str(*[elem.text for elem in my_pets_tabl]).split('\n')[1::2]
        print(list_my_pets)
        pets_image = self.wait.until(EC.presence_of_all_elements_located(
            MyPetsPageLocators.PETS_IMAGE))
        list_image = [1 * (el.get_attribute('src') != '') for el in pets_image][:-1]
        # print(list_image)
        assert len(list_my_pets) == self.pets_amount_before, 'Количество питомцев не совпадает с таблицей'
        assert sum(list_image) / len(list_my_pets) > 0.5, 'Фото не имеют больше 50% питомцев'
        assert all([len(elem.split()) == 3 for elem in list_my_pets]), 'Не все питомцы имеют имя, породу и возраст'
        pet_names = [elem.split()[0] for elem in list_my_pets]
        assert len(pet_names) == len(set(pet_names)), 'Имеются повторяющиеся имена'
        assert len(list_my_pets) == len(set(list_my_pets)), 'Имеются повторяющиеся питомцы'


    def add_new_pet(self, new_pet):
        pet_form = self.wait.until(EC.presence_of_element_located(
            MyPetsPageLocators.ADD_PET_BUTTON))
        pet_form.click()
        pet_name = self.wait.until(EC.presence_of_element_located(
            MyPetsPageLocators.PET_NAME))
        pet_name.send_keys(new_pet['name'])
        animal_type = self.wait.until(EC.presence_of_element_located(
            MyPetsPageLocators.ANIMAL_TYPE))
        animal_type.send_keys(new_pet['animal_type'])
        pet_age = self.wait.until(EC.presence_of_element_located(
            MyPetsPageLocators.PET_AGE))
        pet_age.send_keys(new_pet['age'])
        add_button = self.wait.until(EC.presence_of_element_located(
            MyPetsPageLocators.ADD_BUTTON))
        add_button.click()
        self.browser.refresh()
        page_info = self.wait.until(EC.presence_of_element_located(
            MyPetsPageLocators.PAGE_INFO)).text
        pets_amount_after = int(page_info.split(': ')[1].split('\n')[0])
        print(f'\nКоличество моих питомцев: {pets_amount_after}')
        assert pets_amount_after - self.pets_amount_before == 1, \
            'Карточка нового питомца не добавлена'

    def delete_last_pet(self):
        if self.pets_amount_before > 0:
            how, what = MyPetsPageLocators.DEL_PET
            what = what.replace('$', str(self.pets_amount_before))
            DEL_PET = (how, what)
            last_pet = self.wait.until(EC.presence_of_element_located(DEL_PET))
            last_pet.click()
            self.browser.refresh()
            page_info = self.wait.until(EC.presence_of_element_located(
                MyPetsPageLocators.PAGE_INFO)).text
            pets_amount_after = int(page_info.split(': ')[1].split('\n')[0])
            print(f'\nКоличество моих питомцев: {pets_amount_after}')
            assert pets_amount_after - self.pets_amount_before == -1, \
                'Карточка последнего питомца не удалена'
        else:
            print('Список ваших питомцев пуст')

