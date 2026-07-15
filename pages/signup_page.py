from selenium.webdriver.common.by import By

from base.basis import Base


class SignUpPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_full_name(self,full_name):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='name']"
        ).send_keys(full_name)

    def enter_email(self,email):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='email']"
        ).send_keys(email)

    def enter_password(self,password):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='password']"
        ).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='password_confirmation']"
        ).send_keys(confirm_password)

    def click_submit_button(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def create_account(self,full_name,email,password,confirm_password):
        self.enter_full_name(full_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_submit_button()