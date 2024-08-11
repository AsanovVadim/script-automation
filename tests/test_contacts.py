import pytest
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage


class TestContacts:
    def test_change_region(self, driver):
        main_page = MainPage(driver)
        contacts_page = ContactsPage(driver)

        # Переход на страницу контактов
        main_page.go_to_contacts()

        # Проверка региона и списка партнеров
        current_region = contacts_page.get_region()
        assert current_region == "Ярославская область", f"Ожидали 'Ярославская область', но получили '{current_region}'"

        assert contacts_page.check_partners_list(), "Список партнеров пуст!"

        # Изменение региона на Камчатский край
        contacts_page.change_region("Камчатский край")

        # Проверка нового региона и обновления URL и title
        new_region = contacts_page.get_region()
        assert new_region == "Камчатский край", f"Ожидали 'Камчатский край', но получили '{new_region}'"

        contacts_page.verify_region_and_url(new_region)