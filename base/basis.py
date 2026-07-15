from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_until_element_be_visible(self,locator,path):
        return self.wait.until(
            EC.visibility_of_element_located(
                (
                    locator,
                 path
                 )
            )
        )

    def wait_until_element_be_presence(self,locator,path):
        return self.wait.until(
            EC.presence_of_element_located(
                (
                    locator,
                    path
                )
            )
        )

    def wait_until_element_be_clickable(self,locator,path):
        return self.wait.until(
            EC.element_to_be_clickable(
                (
                    locator,
                    path
                )
            )
        )

    def wait_until_elements_present(self,locator,path):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    locator,
                    path
                )
            )
        )

    def scroll(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    def scroll_to_element(self,element):
        self.driver.execute_script("""
                   const y = arguments[0].getBoundingClientRect().top + window.pageYOffset - 120;
                   window.scrollTo({top: y, behavior: 'instant'});
               """, element)