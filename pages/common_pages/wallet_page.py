from selenium.webdriver.common.by import By

from base.basis import Base


class WalletPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_deposit_amount(self,deposit_amount):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='deposit-amount']"
        ).send_keys(deposit_amount)

    def select_deposit_method(self,deposit_method):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//form[@action='/wallet/deposit']//button[@role='combobox']"
        ).click()
        if deposit_method == "Bank Transfer":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[1]"
            ).click()
        elif deposit_method == "Card":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[2]"
            ).click()
        elif deposit_method == "Crypto":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[3]"
            ).click()

    def click_request_deposit(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[normalize-space()='Request deposit']"
        ).click()

    def create_deposit(self,deposit_amount,deposit_method):
        self.enter_deposit_amount(deposit_amount)
        self.select_deposit_method(deposit_method)
        self.click_request_deposit()

    def enter_withdraw_amount(self,withdraw_amount):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='withdraw-amount']"
        ).send_keys(withdraw_amount)

    def select_withdraw_method(self,withdraw_method):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//form[@action='/wallet/withdraw']//button[@role='combobox']"
        ).click()
        if withdraw_method == "Bank Transfer":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[1]"
            ).click()
        elif withdraw_method == "Card":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[2]"
            ).click()
        elif withdraw_method == "Crypto":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[3]"
            ).click()

    def click_submit_withdraw(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[normalize-space()='Submit withdrawal']"
        ).click()

    def create_withdraw(self,withdraw_amount,withdraw_method):
        self.enter_withdraw_amount(withdraw_amount)
        self.select_withdraw_method(withdraw_method)
        self.click_submit_withdraw()

    def select_from_account(self,from_account):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//button[@role='combobox'])[3]"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            f"(//div[@role='option'])[{from_account}]"
        ).click()

    def select_to_account(self,to_account):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//button[@role='combobox'])[4]"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            f"(//div[@role='option'])[{to_account}]"
        ).click()

    def enter_transfer_amount(self,transfer_amount):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='transfer-amount']"
        ).send_keys(transfer_amount)

    def click_transfer_funds(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[normalize-space()='Transfer funds']"
        ).click()

    def create_transfer(self,from_account,to_account,transfer_amount):
        self.select_from_account(from_account)
        self.select_to_account(to_account)
        self.enter_transfer_amount(transfer_amount)

