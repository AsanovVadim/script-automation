# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()  # Браузер
#     yield driver
#     driver.quit()
#
#
# def test_scenario1(driver):
#     # Переход на SBIS и поиск баннера Tensor
#     driver.get("https://sbis.ru/")
#     driver.find_element(By.LINK_TEXT, "Контакты").click()
#     tensor_banner = driver.find_element(By.XPATH, "//a[contains(text(), 'Tensor')]")  # Селектор
#     tensor_banner.click()
#
#     # Проверка перехода на Tensor и наличие блока "Сила в людях"
#     assert driver.current_url == "https://tensor.ru/"
#     power_in_people_block = driver.find_element(By.XPATH, "//h2[contains(text(), 'Сила в людях')]")  # Селектор
#
#     # Переход в "Подробнее" и проверка ссылки
#     power_in_people_block.find_element(By.LINK_TEXT, "Подробнее").click()
#     assert driver.current_url == "https://tensor.ru/about"
#
#     # Проверка размеров фотографий в разделе "Работаем"
#     # Реализация проверки размеров с помощью Selenium и JavaScriptExecutor:
#     photos = driver.find_elements(By.XPATH, "//div[@class='tensor_ru-About__block3-image new_lazy loaded']")  # Селектор
#     for photo in photos:
#         driver.execute_script("arguments[0].scrollIntoView();", photo)  # Прокрутка до фотографии
#         height = photo.size['height']
#         width = photo.size['width']
#         assert height == 192, f"Высота фотографии не соответствует ожидаемой. " \
#                                           f"Ожидалось: {192}, фактически: {height}"
#         assert width == 270, f"Ширина фотографии не соответствует ожидаемой. " \
#                                         f"Ожидалось: {268.5}, фактически: {width}"
