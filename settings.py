import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_user_name = os.getenv('valid_user_name')

new_pet = {
    'name': 'Luntik',
    'animal_type': 'alien',
    'age': '10'}

