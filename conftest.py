import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Убедитесь, что у вас установлен драйвер Chrome
    yield driver
    driver.quit()