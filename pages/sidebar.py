from selenium.webdriver.common.by import By

from base.basis import Base


class SideBar(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_dashboard(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[1]"
        ).click()

    def click_trading_account(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@href='/accounts']"
        ).click()

    def click_wallet(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@href='/wallet']"
        ).click()

    def click_transactions(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[5]"
        ).click()

    def click_markets(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[6]"
        ).click()

    def click_verification(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[7]"
        ).click()

    def click_account_request(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[8]"
        ).click()

    def click_approve_withdraw(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[9]"
        ).click()

    def click_approve_deposit(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[10]"
        ).click()

    def click_review_kyc(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[11]"
        ).click()

    def click_users(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//a)[12]"
        ).click()

    def click_on_account(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@id='reka-dropdown-menu-trigger-v-109']"
        ).click()

    def click_logout(self):
        self.click_on_account()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[normalize-space()='Log out']"
        ).click()

    def click_settings(self):
        self.click_on_account()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[normalize-space()='Settings']"
        ).click()