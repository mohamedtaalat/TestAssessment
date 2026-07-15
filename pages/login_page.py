from selenium.webdriver.common.by import By

from base.basis import Base


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='email']"
        ).send_keys(email)

    def enter_password(self, password):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='password']"
        ).send_keys(password)

    def click_remember_login(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@id='remember']"
        ).click()

    def click_login(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def click_signup(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-foreground underline decoration-neutral-300 underline-offset-4 transition-colors duration-300 ease-out hover:decoration-current! dark:decoration-neutral-500']"
        ).click()

    def click_forgot_password(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-foreground underline decoration-neutral-300 underline-offset-4 transition-colors duration-300 ease-out hover:decoration-current! dark:decoration-neutral-500 text-sm']"
        ).click()

    def click_signin_with_passkey(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[normalize-space()='Sign in with a passkey']"
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
