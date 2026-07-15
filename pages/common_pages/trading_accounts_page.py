from selenium.webdriver.common.by import By

from base.basis import Base


class TradingAccountsPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def click_request_account(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive h-9 px-4 py-2 has-[>svg]:px-3 bg-emerald-500 text-slate-950 hover:bg-emerald-400']"
        ).click()

class RequestAccountForm(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def select_account_type(self,account_type):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//button[@role='combobox'])[1]"
        ).click()
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
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//button[@role='combobox'])[2]"
        ).click()

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
        self.wait_until_element_be_clickable(
            By.XPATH,
            "(//button[@role='combobox'])[3]"
        ).click()
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
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@id='purpose']"
        ).send_keys(trading_purpose)

    def click_submit(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[normalize-space()='Submit request']"
        ).click()

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