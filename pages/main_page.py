from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_contacts(self):
        self.driver.get("https://sbis.ru/")
        contacts_link = self.driver.find_element(By.LINK_TEXT, "Контакты")
        contacts_link.click()

    def click_tensor_banner(self):
        tensor_banner = self.driver.find_element(By.XPATH, "//a[contains(@href, 'tensor')]")
        tensor_banner.click()