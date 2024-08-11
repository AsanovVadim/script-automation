import pytest
from pages.main_page import MainPage
from pages.tensor_page import TensorPage


class TestTensor:
    def test_tensor_scenario(self, driver):
        main_page = MainPage(driver)
        tensor_page = TensorPage(driver)

        # Сценарий 1
        main_page.go_to_contacts()
        main_page.click_tensor_banner()

        # Проверка блока "Сила в людях"
        tensor_page.verify_people_power_block()

        # Переход в "Подробнее" и проверка URL
        tensor_page.go_to_more_info()
        tensor_page.verify_about_page()

        # Проверка высоты и ширины фотографий
        tensor_page.check_photos_dimensions()