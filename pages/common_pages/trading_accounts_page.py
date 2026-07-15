from selenium.webdriver.common.by import By

from base.basis import Base


class TradingAccountsPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def click_request_account(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[normalize-space()='Request account']"
        ).click()

class RequestAccountForm(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def select_account_type(self,account_type):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "(//button[@role='combobox'])[1]"
        )
        self.scroll_to_element(element)
        element.click()
        if account_type == "demo":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[1]"
            ).click()
        elif account_type == "live":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[2]"
            ).click()

    def select_base_currency(self,base_currency):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "(//button[@role='combobox'])[2]"
        )
        self.scroll_to_element(element)
        element.click()

        if base_currency == "USD":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[1]"
            ).click()
        elif base_currency == "EUR":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[2]"
            ).click()
        elif base_currency == "GBP":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[3]"
            ).click()

    def select_leverage(self,leverage):
        element =  self.wait_until_element_be_clickable(
            By.XPATH,
            "(//button[@role='combobox'])[3]"
        )
        self.scroll_to_element(element)
        element.click()
        if leverage == "1:50":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[1]"
            ).click()
        elif leverage == "1:100":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[2]"
            ).click()
        elif leverage == "1:200":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[3]"
            ).click()
        elif leverage == "1:500":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[4]"
            ).click()

    def enter_trading_purpose(self,trading_purpose):
        element = self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='purpose']"
        )
        self.scroll_to_element(element)
        element.send_keys(trading_purpose)

    def click_submit(self):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[normalize-space()='Submit request']"
        )
        self.scroll_to_element(element)
        element.click()

    def click_cancel(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[normalize-space()='Cancel']"
        ).click()

    def create_account_request(self,account_type,base_currency,leverage,trading_purpose):
        self.select_account_type(account_type)
        self.select_base_currency(base_currency)
        self.select_leverage(leverage)
        self.enter_trading_purpose(trading_purpose)
        self.click_submit()