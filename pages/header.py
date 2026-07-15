from selenium.webdriver.common.by import By

from base.basis import Base


class Header(Base):
    def __init__(self, driver):
        super().__init__(driver)


    def click_services(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-sm text-slate-300 transition hover:text-white'][normalize-space()='Services']"
        ).click()

    def click_about(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-sm text-slate-300 transition hover:text-white'][normalize-space()='About']"
        ).click()


    def click_contact(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-sm text-slate-300 transition hover:text-white'][normalize-space()='Contact']"
        ).click()

    def click_assessment(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-sm text-slate-300 transition hover:text-white'][normalize-space()='Assessment']"
        ).click()

    def click_login(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='hidden text-sm text-slate-300 hover:text-white sm:inline']"
        ).click()

    def click_open_account(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
          "//a[normalize-space()='Open account']"
        ).click()



