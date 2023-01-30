from selenium.webdriver.common.by import By


class AuthPageLocators:
    TITLE = (By.TAG_NAME, 'h1')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'pass')
    SUBMIT_BUTTON = (By.CLASS_NAME, 'btn-success')
    REGISTER_LINK = (By.CSS_SELECTOR, '[href="/new_user"]')


class RegPageLocators:
    TITLE = (By.TAG_NAME, 'h1')
    NAME_FIELD = (By.ID, 'name')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'pass')
    SUBMIT_BUTTON = (By.CLASS_NAME, 'btn-success')
    LOGIN_LINK = (By.CSS_SELECTOR, '[href="/login"]')


class AllPetsPageLocators:
    MY_PETS = (By.CSS_SELECTOR, '[href="/my_pets"]')


class MyPetsPageLocators:
    USER_NAME = (By.TAG_NAME, 'h2')
    PAGE_INFO = (By.CLASS_NAME, 'left')
    ADD_PET_BUTTON = (By.CLASS_NAME, 'btn-outline-success')
    PET_NAME = (By.ID, 'name')
    ANIMAL_TYPE = (By.ID, 'animal_type')
    PET_AGE = (By.ID, 'age')
    PET_PHOTO = (By.ID, 'pet_photo')
    ADD_BUTTON = (By.CLASS_NAME, 'btn-success')
    CANCEL_BUTTON = (By.CLASS_NAME, 'btn-secondary')
    DEL_PET = (By.CSS_SELECTOR, 'tbody>tr:nth-child($)>.smart_cell>a')
    MY_PETS_TABL = (By.ID, 'all_my_pets')
    PETS_IMAGE = (By.TAG_NAME, 'img')

