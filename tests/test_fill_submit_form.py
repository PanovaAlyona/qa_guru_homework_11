import os
import time
from datetime import date

import allure
from selene import browser
from selenium.webdriver.common.devtools.v141.emulation import set_user_agent_override

from qa_guru_homework_11.registration_steps import RegistrationSteps
from qa_guru_homework_11.user import User
from utils import attach


@allure.title("Проверка регистрации пользователя")
@allure.epic("DEMOQA")
@allure.feature("Форма регистрации")
def test_fill_submit_form(setup_browser):
    student = User(
        first_name='Alex',
        last_name='Bagel',
        email='alexbagel@mail.ru',
        gender='Male',
        mobile_number='9021778990',
        date_of_birth=date(1990, 6, 19),
        subject='English',
        hobbies='Sports',
        picture=os.path.join(os.path.dirname(os.path.dirname(__file__)),'mount.jpg'),
        street_address='Lomonosov str. 8',
        state_address='Haryana',
        city_address='Panipat'
    )

    registration_steps = RegistrationSteps(setup_browser)

    registration_steps.open()
    registration_steps.register(student)
    registration_steps.should_have_registered(student)

    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
