from selenium.webdriver.common.by import By


class TensorPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_people_power_block(self):
        assert self.driver.find_element(By.XPATH, "//h2[text()='Сила в людях']")

    def go_to_more_info(self):
        more_info_link = self.driver.find_element(By.LINK_TEXT, "Подробнее")
        more_info_link.click()

    def verify_about_page(self):
        assert self.driver.current_url == "https://tensor.ru/about"

    def check_photos_dimensions(self):
        photos = self.driver.find_elements(By.CSS_SELECTOR, ".timeline-photo img")
        heights = [photo.size['height'] for photo in photos]
        widths = [photo.size['width'] for photo in photos]

        assert len(set(heights)) == 1, "Высота фотографий не одинаковая"
        assert len(set(widths)) == 1, "Ширина фотографий не одинаковая"