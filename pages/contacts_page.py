from selenium.webdriver.common.by import By


class ContactsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_region(self):
        region_element = self.driver.find_element(By.CSS_SELECTOR, ".region-selector")
        return region_element.text

    def check_partners_list(self):
        partners_list = self.driver.find_element(By.CSS_SELECTOR, ".partners-list")
        return len(partners_list.find_elements(By.TAG_NAME, "li")) > 0

    def change_region(self, new_region):
        region_selector = self.driver.find_element(By.CSS_SELECTOR, ".region-selector")
        region_selector.click()
        new_region_option = self.driver.find_element(By.XPATH, f"//option[text()='{new_region}']")
        new_region_option.click()

    def verify_region_and_url(self, expected_region):
        assert expected_region in self.driver.title
        assert expected_region in self.driver.current_url